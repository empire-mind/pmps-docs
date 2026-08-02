from dataclasses import dataclass

REQUIRED_METADATA = (
    "client_id", "project_id", "record_class", "authority_system",
    "sensitivity", "retention_rule", "owner",
)

@dataclass(frozen=True)
class PolicyDecision:
    outcome: str
    route_key: str
    reason_codes: tuple[str, ...]
    approval_required: bool

def decide(metadata: dict, confidence: float, config: dict) -> PolicyDecision:
    missing = [key for key in REQUIRED_METADATA if not metadata.get(key)]
    controls = config["routing"]
    route_key = config.get("class_routes", {}).get(metadata.get("record_class"), "intake")
    route = config["routes"].get(route_key)
    reasons: list[str] = []
    if missing:
        reasons.append("MISSING_REQUIRED_METADATA")
    if confidence < float(controls["minimum_confidence"]):
        reasons.append("LOW_CONFIDENCE")
    if route is None or not route.get("drive_folder_id"):
        reasons.append("UNRESOLVED_ROUTE")
    elif route.get("enabled") is False:
        reasons.append("ROUTE_NOT_ENABLED")
    if metadata.get("record_class") in set(controls["always_human_gated_classes"]):
        reasons.append("HUMAN_GATE_REQUIRED")
    exception_codes = {"MISSING_REQUIRED_METADATA", "LOW_CONFIDENCE",
                       "UNRESOLVED_ROUTE", "ROUTE_NOT_ENABLED"}
    if exception_codes.intersection(reasons):
        return PolicyDecision("EXCEPTION", "intake", tuple(reasons), True)
    if reasons:
        return PolicyDecision("APPROVAL_REQUIRED", route_key, tuple(reasons), True)
    return PolicyDecision("ROUTE_PROPOSED", route_key,
                          ("DETERMINISTIC_ROUTE_MATCH",), False)
