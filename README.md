# PMPS Document Control

This private repository is the machine-readable control package for Premium Mobile Plant Solutions Pty Ltd document governance.

## Authority boundaries

- Google Drive controlled masters plus the Master Document Register are authoritative for business documents.
- Notion is the human-facing control room and must project, not replace, the register.
- GitHub controls schemas, routing policy, validation, tests and migration configuration.
- Xero, JobAdder, TrackEasy and nominated operational systems remain authoritative for their transactional records.

No employee-facing controlled master, worker personal information, finance evidence, credentials or signed legal material belongs in this repository.

## Locked foundation

- One Shared Drive.
- One intake lane: `99 INTAKE`.
- One controlled-document identity per concept.
- Deterministic routing from stable Drive IDs and metadata.
- Human approval for issue, supersession, disposal, financial, legal, WHS, HR and access decisions.
- SHA-256 before migration or duplicate decisions.
- No production migration until the pilot and access tests pass.

## Repository map

```text
config/control-room.yaml       Canonical authority, folders, states and gates
config/document-library.yaml   Required document families and build waves
schemas/record.schema.json     Record metadata contract
schemas/event.schema.json      Auditable event contract
docs/CONTROL-ROOM.md           Human operating view
docs/MIGRATION-PLAYBOOK.md     Bounded migration procedure
scripts/validate_control.py    Offline configuration validator
tests/test_control.py          Golden control tests
```

## Validate

```powershell
python scripts/validate_control.py
python -m unittest discover -s tests -v
```

## Current truth

This package defines the approved control design. It does not prove production runtime, folder permissions, document approval, migration completion or deletion authority. Those require external readback and approval receipts.
