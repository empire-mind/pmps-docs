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
