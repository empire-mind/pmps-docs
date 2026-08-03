"""Intake / approval runtime for PMPS document control."""

from __future__ import annotations

import hashlib
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .ledger import Ledger
from .policy import decide


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _base_event(
    *,
    record_id: str,
    content_hash: str,
    policy_version: str,
    source_name: str | None = None,
) -> dict[str, Any]:
    event: dict[str, Any] = {
        "record_id": record_id,
        "occurred_at": _now(),
        "actor_type": "system",
        "actor_id": "pmps-control-v1",
        "policy_version": policy_version,
        "sha256": content_hash,
    }
    if source_name is not None:
        # Portable name only — never full host paths in the ledger.
        event["source_name"] = source_name
    return event


def intake(
    source: Path,
    metadata: dict[str, Any],
    confidence: float,
    config: dict[str, Any],
    ledger: Ledger,
) -> dict[str, Any]:
    """Fingerprint, route, append ledger events. Idempotent on content hash."""
    source = Path(source)
    content_hash = digest(source)

    prior = ledger.find_by_content_hash(content_hash)
    if prior:
        prior_record_id = prior[0]["record_id"]
        events = ledger.replay(prior_record_id)
        route_events = [e for e in events if e.get("event_type") == "route.proposed"]
        last_route = route_events[-1] if route_events else {}
        return {
            "record_id": prior_record_id,
            "sha256": content_hash,
            "outcome": last_route.get("outcome", "DECISION_ALREADY_RECORDED"),
            "route_key": last_route.get("route_key", "intake"),
            "approval_required": bool(
                last_route.get("outcome") in {"APPROVAL_REQUIRED", "EXCEPTION"}
            ),
            "reason_codes": list(
                last_route.get("reason_codes") or ["DECISION_ALREADY_RECORDED"]
            ),
            "duplicate": True,
            "events_replayed": len(events),
        }

    record_id = metadata.get("record_id") or f"PMPS-REC-{uuid.uuid4()}"
    decision = decide(metadata, confidence, config)
    base = _base_event(
        record_id=record_id,
        content_hash=content_hash,
        policy_version=config["policy_version"],
        source_name=source.name,
    )
    received = {
        **base,
        "event_id": str(uuid.uuid4()),
        "event_type": "record.received",
        "reason_codes": ["INTAKE_ACCEPTED"],
    }
    proposed = {
        **base,
        "event_id": str(uuid.uuid4()),
        "event_type": "route.proposed",
        "route_key": decision.route_key,
        "outcome": decision.outcome,
        "reason_codes": list(decision.reason_codes),
    }
    ledger.append_many([received, proposed])
    return {
        "record_id": record_id,
        "sha256": content_hash,
        "outcome": decision.outcome,
        "route_key": decision.route_key,
        "approval_required": decision.approval_required,
        "reason_codes": list(decision.reason_codes),
        "duplicate": False,
    }


def record_approval(
    record_id: str,
    *,
    decision: str,
    approver: str,
    content_hash: str,
    version: str,
    config: dict[str, Any],
    ledger: Ledger,
    document_id: str | None = None,
) -> dict[str, Any]:
    """Append an approval.recorded event bound to the content hash."""
    decision_norm = decision.strip().upper()
    if decision_norm not in {"APPROVED", "REJECTED"}:
        raise ValueError("decision must be APPROVED or REJECTED")
    base = _base_event(
        record_id=record_id,
        content_hash=content_hash,
        policy_version=config["policy_version"],
    )
    event = {
        **base,
        "event_id": str(uuid.uuid4()),
        "event_type": "approval.recorded",
        "decision": decision_norm,
        "approver": approver,
        "document_id": document_id or record_id,
        "version": version,
        "actor_type": "human",
        "actor_id": approver,
        "reason_codes": ["HUMAN_APPROVAL_RECORDED"],
    }
    ledger.append(event)
    return {
        "record_id": record_id,
        "sha256": content_hash,
        "decision": decision_norm,
        "approver": approver,
        "version": version,
        "document_id": document_id or record_id,
        "event_id": event["event_id"],
    }
