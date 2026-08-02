import hashlib
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .ledger import Ledger
from .policy import decide

def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()

def intake(source: Path, metadata: dict, confidence: float, config: dict, ledger: Ledger) -> dict:
    record_id = metadata.get("record_id") or f"PMPS-REC-{uuid.uuid4()}"
    content_hash = digest(source)
    decision = decide(metadata, confidence, config)
    now = datetime.now(timezone.utc).isoformat()
    base = {"record_id": record_id, "occurred_at": now, "actor_type": "system",
            "actor_id": "pmps-control-v1", "policy_version": config["policy_version"],
            "sha256": content_hash}
    received = {**base, "event_id": str(uuid.uuid4()), "event_type": "record.received",
                "source_path": str(source), "reason_codes": ["INTAKE_ACCEPTED"]}
    proposed = {**base, "event_id": str(uuid.uuid4()), "event_type": "route.proposed",
                "route_key": decision.route_key, "outcome": decision.outcome,
                "reason_codes": list(decision.reason_codes)}
    ledger.append(received)
    ledger.append(proposed)
    return {"record_id": record_id, "sha256": content_hash,
            "outcome": decision.outcome, "route_key": decision.route_key,
            "approval_required": decision.approval_required,
            "reason_codes": list(decision.reason_codes)}

def approve_record(record_id: str, approver: str, config: dict, ledger: Ledger) -> dict:
    events = ledger.replay(record_id)
    if not events:
        raise ValueError(f"Unknown record_id: {record_id}")
    latest = events[-1]
    now = datetime.now(timezone.utc).isoformat()
    base = {"record_id": record_id, "occurred_at": now, "actor_type": "human",
            "actor_id": approver, "policy_version": config["policy_version"],
            "sha256": latest["sha256"]}
    approved = {**base, "event_id": str(uuid.uuid4()), "event_type": "route.approved",
                "status": "APPROVED"}
    canonical = {**base, "event_id": str(uuid.uuid4()), "event_type": "filed.canonical",
                 "canonical_vault_path": f"03-Projects/pty-ltd/premium-mobile-plant-solutions/docs/{record_id}.md"}
    ledger.append(approved)
    ledger.append(canonical)
    return {"record_id": record_id, "status": "APPROVED", "canonical_vault_path": canonical["canonical_vault_path"]}

def cite_record(record_id: str, retriever: str, ledger: Ledger) -> dict:
    events = ledger.replay(record_id)
    if not events:
        raise ValueError(f"Unknown record_id: {record_id}")
    latest = events[-1]
    now = datetime.now(timezone.utc).isoformat()
    citation_hash = hashlib.sha256(f"{record_id}:{latest['sha256']}:{now}".encode("utf-8")).hexdigest()
    cited = {
        "event_id": str(uuid.uuid4()), "record_id": record_id, "occurred_at": now,
        "actor_type": "agent", "actor_id": retriever, "event_type": "retrieved.cited",
        "sha256": latest["sha256"], "citation_hash": citation_hash
    }
    ledger.append(cited)
    return {"record_id": record_id, "citation_hash": citation_hash, "sha256": latest["sha256"]}

def supersede_record(old_record_id: str, new_record_id: str, reason: str, ledger: Ledger) -> dict:
    events = ledger.replay(old_record_id)
    if not events:
        raise ValueError(f"Unknown record_id: {old_record_id}")
    latest = events[-1]
    now = datetime.now(timezone.utc).isoformat()
    superseded = {
        "event_id": str(uuid.uuid4()), "record_id": old_record_id, "occurred_at": now,
        "actor_type": "human", "actor_id": "document-controller", "event_type": "record.superseded",
        "superseded_by": new_record_id, "reason": reason, "sha256": latest["sha256"]
    }
    ledger.append(superseded)
    return {"record_id": old_record_id, "status": "SUPERSEDED", "superseded_by": new_record_id}

def restore_record(record_id: str, ledger: Ledger) -> dict:
    events = ledger.replay(record_id)
    if not events:
        raise ValueError(f"Unknown record_id: {record_id}")
    # Verify hash consistency across all events
    first_hash = events[0]["sha256"]
    for evt in events:
        if evt["sha256"] != first_hash:
            raise ValueError(f"Ledger tampering detected for {record_id}")
    now = datetime.now(timezone.utc).isoformat()
    restored = {
        "event_id": str(uuid.uuid4()), "record_id": record_id, "occurred_at": now,
        "actor_type": "system", "actor_id": "recovery-engine", "event_type": "record.restored",
        "sha256": first_hash, "restored_events_count": len(events)
    }
    ledger.append(restored)
    return {"record_id": record_id, "status": "RESTORED", "verified_sha256": first_hash, "event_count": len(events) + 1}
