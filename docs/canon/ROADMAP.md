# ROADMAP — Solid PMPS Foundations

**ID:** `PMPS-PLN-GOV-001`  
**Goal:** Premium, boringly reliable document foundation — not more parallel systems.  
**Linear home:** Project *PMPS Foundations Program* (same board as pilot; roadmap issues tagged `roadmap`)

---

## Definition of “Solid Foundation”

All true together:

1. One Drive Controlled Workspace exists and is the only place for ACTIVE masters.  
2. Master Document Register is live; every ACTIVE doc has ID + version + hash + link.  
3. Notion Approved Docs list mirrors Register (no extras that aren’t in Register).  
4. Human SOP is known and used (this pack).  
5. Brand/design path works (`pmps-design-system` tests green + one issued sample).  
6. `pmps-docs` **main** has control engine + this canon (not empty).  
7. Obsidian only mirrors canon pointers.  
8. Linear roadmap issues are the delivery backlog — no shadow plans in chat.  
9. Gap list exists (required library vs inventory) with owners.  
10. No finance/HR/legal auto-issue.

---

## Phase 0 — Freeze truth (Week 1)  ← YOU ARE HERE

| ID | Deliverable | Owner | Evidence |
|----|-------------|-------|----------|
| R0.1 | Merge `pmps-docs` PR #1 (engine + STATUS + this canon) | Eli | main has docs/canon |
| R0.2 | Publish CANON + HUMAN-SOP; announce “this supersedes conflicting notes” | Eli | Git + Notion pointer page |
| R0.3 | Confirm Drive Shared Drive + Foundations root IDs | Eli/Ash | Open folder live |
| R0.4 | Create / confirm **Controlled Workspace** folder set (DRIVE-WORKSPACE) | Eli | Screenshots or folder IDs in Register |
| R0.5 | Create Master Document Register sheet from schema | Eli/Ash | Sheet link in START HERE |
| R0.6 | Create Notion **Approved Documents** database | Eli | DB URL |
| R0.7 | Obsidian mirror folder + CANON pointer note | Eli | Vault path |
| R0.8 | Linear project description = this roadmap; milestones = phases | Eli | Linear updated |
| R0.9 | SUPERSEDED-INDEX lists old plans | Eli | This pack |

**Exit:** Anyone can answer “where is the official copy?” in one sentence.

---

## Phase 1 — First official docs (Weeks 1–3)

| ID | Deliverable | Owner | Evidence |
|----|-------------|-------|----------|
| R1.1 | Issue **Human SOP** as ACTIVE (this file, branded PDF/DOCX optional) | Ash approve | Register row |
| R1.2 | Issue **Document Control SOP** shell (or promote existing candidate) | Ash | Register |
| R1.3 | Issue **File Plan / Workspace map** (DRIVE-WORKSPACE) | Ash/Eli | Register |
| R1.4 | Seed Register with minimum library from `document-library.yaml` (FOUND/GAP) | Eli | ≥15 rows |
| R1.5 | One low-risk operational checklist fully through SOP path | Ash | Hash + Drive + Notion |
| R1.6 | pmps-design-system: tag release if CI green | Eli | Git tag |

**Exit:** At least 3 ACTIVE_CANONICAL docs; path proven end-to-end by humans.

---

## Phase 2 — Inventory & gaps (Weeks 2–5)

| ID | Deliverable | Owner | Evidence |
|----|-------------|-------|----------|
| R2.1 | Read-only discovery of existing docs (Drive + legacy SharePoint + Desktop exports) | Eli | Manifest CSV (metadata only) |
| R2.2 | Gap analysis v1: required library vs found | Both | Gap register in Drive Governance |
| R2.3 | Prioritised close-gap backlog in Linear (WHS → Ops → Workforce → Finance) | Ash | Ranked issues |
| R2.4 | Mark dangerous duplicates SUPERSEDED in Register | Ash | Register updates |

**Exit:** No unknown “which contract/SOP is real?” for top 20 processes.

---

## Phase 3 — Engine hardening (Weeks 3–6, parallel after R0.1)

| ID | Deliverable | Owner | Evidence |
|----|-------------|-------|----------|
| R3.1 | Idempotent intake + hash-chained ledger | Eli | tests |
| R3.2 | Approval receipt event bound to hash | Eli | tests |
| R3.3 | Read-only Drive list/hash adapter | Eli | commissioning receipt |
| R3.4 | Write+readback behind explicit approve flag | Eli | receipt |
| R3.5 | Stop claiming lifecycle stages not implemented | Eli | README honesty |

**Exit:** Machine assists humans; humans still approve.

---

## Phase 4 — Scale library (Weeks 6–12)

| ID | Deliverable | Owner | Evidence |
|----|-------------|-------|----------|
| R4.1 | Close P0 gaps: WHS policies/SOPs under control | Ash + competent review | Register |
| R4.2 | Workforce templates (blank) before personal records | Ash | Register; restricted stays gated |
| R4.3 | Finance procedure docs (not transactional data) | Ash/Eli | Register |
| R4.4 | Quarterly review calendar running | Ash | review_due_date field used |
| R4.5 | Optional: automated gap assist (Slice 3) only after Phase 3 | Eli | design note |

**Exit:** “Solid foundation” checklist (§ top) all green with evidence links.

---

## Phase 5 — Keep it clean (ongoing)

- Monthly: Register ↔ Notion sync audit  
- Quarterly: DR / restore of Drive + Register export  
- Any new AI feature must read CANON.md first or it does not ship  

---

## Milestone mapping (Linear)

| Linear milestone name | = Roadmap phase |
|----------------------|-----------------|
| M0 Freeze Truth | Phase 0 |
| M1 First Official Docs | Phase 1 |
| M2 Inventory & Gaps | Phase 2 |
| M3 Engine Assist | Phase 3 |
| M4 Library Scale | Phase 4 |
| M5 Steady State | Phase 5 |

---

## What we deliberately delay

- Bulk auto-migration of entire estate  
- SharePoint as new controlled primary  
- Full Temporal/OPA stack before Phase 3 basics  
- Agent-only publication  
- Second “Foundations” Drive tree  

**Revision:** 2026-08-03.r1
