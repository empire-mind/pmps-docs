# PMPS Document Control (`pmps-docs`)

Machine-readable **control plane** and program status for Premium Mobile Plant Solutions document governance.

> **Status:** Feature branch carries V1 engine; default `main` was empty until merge of that work.  
> **CANON (single SoT):** [docs/canon/CANON.md](docs/canon/CANON.md) · [HUMAN-SOP](docs/canon/HUMAN-SOP.md) · [ROADMAP](docs/canon/ROADMAP.md)
>
> Also: [STATUS](docs/STATUS.md) · [PATH-FORWARD](docs/PATH-FORWARD.md) (reference detail)

## What this repo is

- Policy/config for filing and human gates  
- Runnable control CLI (`pmps-control`) for intake + ledger replay  
- Architecture and build slices for the wider Foundations engine  

## What this repo is not

- **Not** the brand/design system → see [`pmps-design-system`](https://github.com/empire-mind/pmps-design-system)  
- **Not** the prose control standard pack → EmpireMind vault `Domain Experts/Business Document Control`  
- **Not** the AI memory brain → [`pmps-ai-memory`](https://github.com/empire-mind/pmps-ai-memory)  
- **Not** controlled file storage → Google Drive / approved DMS  

## Authority boundaries

| Surface | Role |
|---------|------|
| Google Drive (or approved DMS) | Controlled masters + evidence bytes |
| Master Document Register | Document identity and lifecycle state |
| This repo (GitHub) | Schemas, routing policy, validation, tests, automation |
| Notion / Linear | Human projections and delivery — not SoT for controlled docs |
| Xero / JobAdder / TrackEasy | Transactional authority in their domains |

No employee-facing controlled master, worker PII, finance evidence, credentials, or signed legal material belongs in this repository.

## Quick start (V1)

```bash
python -m venv .venv && source .venv/bin/activate   # or Windows equivalent
pip install -e . pytest
pytest -q
pmps-control intake ./sample.txt --metadata meta.json --confidence 0.99
pmps-control replay <record_id>
```

## Repository map (actual tree)

```text
config/control-room.yaml     Authority, folders, gates, lifecycle names
config/document-library.yaml Minimum library + build waves (incl. GAP rows)
config/runtime.yaml          Route table + confidence thresholds
src/pmps_control/            CLI, policy, ledger, intake runtime
tests/test_runtime.py
docs/STATUS.md               Program-wide GitHub-grounded status
docs/PATH-FORWARD.md         Clean delivery path
docs/ARCHITECTURE-BLUEPRINT.md
docs/BUILD-PLAN.md
docs/ADR-001-OPEN-SOURCE-STACK.md
Dockerfile / compose.yaml    Hardened offline control container
```

## Related repositories

| Repo | Layer |
|------|--------|
| [pmps-design-system](https://github.com/empire-mind/pmps-design-system) | Document **design** (brand, validator, skill) |
| [pmps-core](https://github.com/empire-mind/pmps-core) | Enterprise / product canon (md) |
| [pmps-ai-memory](https://github.com/empire-mind/pmps-ai-memory) | AI memory and skills |
| [librarian](https://github.com/empire-mind/librarian) | Estate inventory (gap inputs) |
| [pmps-evidence](https://github.com/empire-mind/pmps-evidence) | Evidence binder |
| [pmps-runbooks](https://github.com/empire-mind/pmps-runbooks) | Human ops procedures |

## Current truth

This package defines control design and a **thin** runnable intake/replay path.  
It does **not** by itself prove production Drive permissions, owner approval, migration completion, gap-analysis automation, or full lifecycle issuance. Those require external readback and the path in `docs/PATH-FORWARD.md`.
