# PMPS Foundations — Clean Path Forward

**Companion:** [STATUS.md](./STATUS.md)  
**Date:** 2026-08-03  
**Goal:** One coherent program, one authority map, sequential delivery — no parallel “truths.”

---

## 0. North star (one sentence)

**Discover what documents exist → know what’s missing (gaps) → design branded controlled drafts → issue them under a register with proof — without finance/HR/legal autopilot.**

---

## 1. Freeze the authority map (do this once)

| Concern | Authority | Not authority |
|---------|-----------|----------------|
| Brand / visual design contract | **`pmps-design-system`** (Git + tags) | Random Canva/provider themes |
| Control standard (register rules, statuses, gates) | **BDC Domain Expert pack** (vault) until promoted into `pmps-docs/docs/standard/` | Chat memory |
| Automation / schemas / policy-as-code | **`pmps-docs`** (after main has content) | Desktop-only folders |
| Controlled file bytes | **Google Drive** (post-migration primary) *or* SharePoint only if explicitly re-chosen | Notion, Linear, Git |
| Delivery tracking | **Linear** | — |
| AI working memory | **pmps-ai-memory** (facts) | Not a document register |
| Enterprise product/strategy canon | **pmps-core** (read; don’t silently fork) | — |
| Estate inventory | **librarian** catalog | — |
| Evidence receipts | **pmps-evidence** | — |

**Decision still required (Eli + Ashley):** Google Drive as long-term controlled store vs finish SharePoint control build (BDC Next Gate 4). Until decided, **no bulk migration automation**.

---

## 2. Workstreams (parallel only where safe)

### WS1 — Make Git match reality (this week)

| # | Action | Owner | Done when |
|---|--------|-------|-----------|
| 1.1 | Merge https://github.com/empire-mind/pmps-docs/pull/1 | Eli | `main` contains engine+docs; clone default works |
| 1.2 | Refresh ATLAS row for pmps-docs / design-system | Eli | ATLAS matches git |
| 1.3 | Merge or close pmps-design-system open CI PRs (#1–#3) | Eli | CI green on main |
| 1.4 | Tag `pmps-design-system` v0.1.0 if tests stay green | Eli | Tag + release notes |
| 1.5 | Kill empty-scaffold confusion: README on empty repos (`pmps-templates`, `pmps-infra`) state EMPTY + pointer | Eli | No fake “planned live” |

### WS2 — Document design (already strongest leg)

| # | Action | Owner | Done when |
|---|--------|-------|-----------|
| 2.1 | MOC status DRAFT → ACTIVE after one real artifact cycle | Eli / Ash visual | DEC + visual approval receipt |
| 2.2 | Produce **one** controlled template pack via skill (e.g. SOP shell or checklist) | Design skill | Validator pass + visual QA JSON |
| 2.3 | Record install hash of deployed skill on operator machines | Eli | Readback ≠ “we copied a folder” |
| 2.4 | Keep brand EMP-540 / PMPS-STD-BRAND-001 aligned with `brand-contract.json` | Eli | Fingerprints match |

### WS3 — Control standard (BDC pack → actionable register)

| # | Action | Owner | Done when |
|---|--------|-------|-----------|
| 3.1 | Gate: **read-only document estate discovery** | Eli approve | Discovery runbook executed; candidate list with sources |
| 3.2 | Stand up **Master Document Register** (schema already in pack) in Drive/Sheets | Doc controller | Register exists; empty rows OK |
| 3.3 | Import known GAP/FOUND rows from `pmps-docs` `document-library.yaml` into register | Eli/Ash | Register ≥ library minimum set |
| 3.4 | Defer SharePoint build until storage decision (see §1) | both | Written decision |

### WS4 — Gap analysis (manual now → automated later)

| # | Action | Owner | Done when |
|---|--------|-------|-----------|
| 4.1 | **Manual v1:** matrix = required library (document-library + BDC standards) vs Librarian/Drive inventory | Eli | Gap list with ID, risk, owner |
| 4.2 | Prioritise gaps: Governance/WHS → Ops → Workforce → Finance | Ash/Eli | Ordered backlog in Linear **one** project |
| 4.3 | **Automated later (Slice 3):** only after WS5 intake+corpus ingest works | eng | `gap_finding` events with evidence locators |

Do **not** build Slice 3 agents before register + design + basic control plane are honest on `main`.

### WS5 — Control plane engine (`pmps-docs`)

Order matters:

| Phase | Build | Exit |
|-------|-------|------|
| **P0** | Merge V1; fix README to match tree | Honest main |
| **P1** | Idempotent intake (content-hash); hash-chained ledger; `pmps-control verify` | Mutation detected by test |
| **P2** | JSON schemas for record/event/approval; load `control-room.yaml` | Schema tests |
| **P3** | Lifecycle states: review → approval_required → approved → issued (still local/Drive-optional) | Replay full chain |
| **P4** | Read-only Drive adapter (list/get/hash); **no write** | Matches config folder IDs |
| **P5** | Write + readback behind human approval flag | Commissioning receipt |
| **P6** | Slice 2 corpus ingest (ClamAV/Docling/etc. per ADR) | Golden fixtures |
| **P7** | Slice 3–5 gap + interview + draft handoff **calling design-system**, not reimplementing brand | Integration test |

### WS6 — Single delivery project (process hygiene)

Use **one** Linear initiative/project for Foundations engineering (Session Control design already describes this pattern).  

- Issues = concrete build/discovery tasks with acceptance criteria + evidence links  
- No transcript dumping  
- No second shadow status in Notion without link to Git STATUS.md  

---

## 3. 30 / 60 / 90 day outcomes

### 30 days — “Honest spine”

- [ ] `pmps-docs` main = real code  
- [ ] STATUS.md + this PATH-FORWARD on main  
- [ ] Design-system tagged; one approved sample artifact  
- [ ] Master Document Register exists (even thin)  
- [ ] Manual gap list v1 published (link in STATUS)  
- [ ] Storage decision recorded (Drive vs SharePoint primary)

### 60 days — “Closed loop dry-run”

- [ ] Hash-chained ledger + approval receipt events  
- [ ] One end-to-end **offline** path: gap → design draft → intake → approve → issue record (Drive write optional)  
- [ ] Librarian (or Drive read-only) inventory feeds gap sheet  
- [ ] Empty scaffolds either filled or archived

### 90 days — “Commissioned thin production”

- [ ] Read-only Drive commissioned  
- [ ] First **online** controlled issue with readback  
- [ ] Gap analysis refreshed from live inventory  
- [ ] Only then schedule bulk migration batches  

---

## 4. Explicit non-goals (until spine is honest)

- Full Temporal/OPA/Postgres stack before P0–P3  
- Bulk estate move  
- Finance/payroll/HR automation  
- Treating Notion as document SoT  
- New parallel “Foundations” repos  
- Claiming 100/100 / ISO certified without proofs scorecard moves off zero  

---

## 5. Immediate next three commands (human)

1. **Eli:** Merge `pmps-docs` PR #1  
2. **Eli:** Tag or CI-merge `pmps-design-system`  
3. **Eli+Ash:** 30-minute decision — Drive vs SharePoint as controlled primary + approve discovery gate  

Then engineering continues on WS5 P1 without waiting for bulk discovery.
