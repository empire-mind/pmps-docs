# PMPS Foundations — Program Status (GitHub-grounded)

**As of:** 2026-08-03  
**Scope:** Whole Foundations / document-control / document-design program  
**Evidence rule:** PROVEN = live command/API this audit · DECLARED = written claim · UNVERIFIED · EMPTY · BLOCKED  
**Not in scope of this note:** day-to-day Ashley pilot tickets (Linear PMP-7x/8x/9x). Those are one delivery surface; this is the estate map.

---

## 1. What “Foundations” actually is

Four layers that people keep mixing up:

| Layer | Plain English | Canonical GitHub / vault home | Maturity |
|-------|----------------|-------------------------------|----------|
| **A. Control standard** | Rules: register, statuses, who can approve, what “canonical” means | `EmpireMind.ai` → `Domain Experts/Business Document Control/` | **Static pack PROVEN**; live mastery **NOT PROVEN** |
| **B. Document design** | Brand + templates + validator so docs look/act like PMPS | `empire-mind/pmps-design-system` | **Code on main PROVEN**; MOC still **DRAFT**; release deploy **UNVERIFIED** |
| **C. Control plane engine** | Machine intake, hash, route, ledger, later lifecycle/Drive | `empire-mind/pmps-docs` | **V1 stub on feature branch PROVEN**; **main EMPTY** |
| **D. Business corpus & ops canon** | SOPs, runbooks, memory, evidence, enterprise docs | `pmps-core`, `pmps-ai-memory`, `pmps-runbooks`, `pmps-evidence`, `librarian` | **Partial / fragmented** |

**Gap analysis** is not a fifth repo. It is a **capability** that sits between corpus truth (D + Librarian) and design/control (B + A + C):

```text
Discover what exists (Librarian / Drive / SharePoint / vault)
        → compare to required library & obligations (Gap analysis)
        → design missing/changed docs (pmps-design-system)
        → control/issue them (standard + control plane + Drive)
```

---

## 2. Repository scorecard (live GitHub)

| Repo | Role | Default branch reality | Last push (API) | Tests this audit | Open PRs | Verdict |
|------|------|------------------------|-----------------|------------------|----------|---------|
| **pmps-design-system** | Document design skill + brand contract + eval registry | Full tree on `main` | 2026-07-28 | skill 3/3 · eval 5/5 · validator pass · registry valid | 3 (CI/deps) | **Primary design home — furthest along** |
| **pmps-docs** | Control-plane engine + filing config | `main` = `.gitignore` only; engine on `codex/lock-pmps-document-control-room` @ `bd98fb6` | 2026-08-02 | 4/4 on feature branch | **#1** merge V1→main | **Engine orphaned off main** |
| **pmps-core** | “Canonical enterprise repo” (ISO folder tree) | Large md tree | 2026-07-27 (mostly Dependabot) | n/a md | 7 | **Historical SoT; ATLAS: snapshot stale 2026-04-18** |
| **pmps-ai-memory** | AI memory / skills / templates (“pmps-brain”) | Live md+skills | 2026-07-03 | n/a | 0 | **Colleague context; overlaps core/Notion** |
| **pmps-runbooks** | Operational procedures (no secrets) | Live | 2026-07-03 | n/a | 1 | **Ops procedures, not doc control engine** |
| **pmps-evidence** | Append-only evidence / snapshots | Partial | 2026-07-19 | n/a | 3 | **Evidence binder; not design** |
| **pmps-finance** | Finance OS UI/scripts | Live | 2026-07-27 | n/a | 1 | **Adjacent finance product; not Foundations core** |
| **librarian** | Estate capture → catalog.db | Live | 2026-07-06 | n/a | 1 | **Corpus inventory feed for gap analysis** |
| **EmpireMind.ai** | Obsidian vault incl. Domain Expert packs | Live | 2026-08-02 | n/a | many | **BDC domain pack + ATLAS registry** |
| **pmps-templates** | Org template for pmps-* | `.gitignore` only | 2026-07-02 | — | 0 | **EMPTY scaffold** |
| **pmps-infra** | Terraform / LaunchAgents planned | empty-ish | 2026-07-02 | — | 0 | **EMPTY scaffold (ATLAS)** |
| **pmps-migration** | M365→Google runbooks | runbooks only | 2026-07-02 | — | 0 | **Migration docs; not Foundations engine** |

### ATLAS (vault) already said this about pmps-docs

> `pmps-docs` … STATE: empty scaffold (only .gitignore) … intent-only, zero content  

That matched **main** until 2026-08-02 when V1 landed on a **non-default branch** (still not main).

---

## 3. Layer detail

### A — Control standard (`Business Document Control` pack)

**Path:** `EmpireMind.ai/Domain Experts/Business Document Control/`  
**Claim ledger (pack’s own):** local pack PROVEN · full live production mastery NOT PROVEN · 100/100 NOT PROVEN  
**Proofs scorecard:** scaffolded zeros (reclassify pass not done)  
**Locked rule:** *If a document is not in the register, it is not canonical.*  
**Next gates (written 2026-07-10):**

1. Approve read-only document estate discovery  
2. Approve contracts specialist source bank  
3. Approve canonical contract register  
4. Approve SharePoint document control build (after discovery)

SharePoint is explicitly **one storage bridge**, not the standard itself.

### B — Document design (`pmps-design-system`)

**What it is:** `pmps-designer` skill — brand contract, CSS tokens, retained masters (PDF/DOCX/logo), deterministic validator, provider adapters, evaluation registry (Drive/Linear/Xero/GitHub/designer capabilities + golden/adversarial cases).

**Decisions locked (DEC-001…005):** Git = editable source; brand outranks providers; Ashley visual / Eli structural; no secrets in git; no silent drift.

**MOC status:** **DRAFT**  
**Architecture:** AAAK/Obsidian → GitHub contract → installed skill → generate → validate + visual QA → READY FOR VISUAL APPROVAL → APPROVED  

**Verified this audit:** unit tests + eval registry + fixture validator all green.

### C — Control plane (`pmps-docs`)

**On feature branch only:**

- `pmps-control` CLI: `intake` | `replay`  
- SHA-256 · routing policy · SQLite ledger (not hash-chained)  
- `config/control-room.yaml`, `document-library.yaml`, `runtime.yaml`  
- Blueprint: `ARCHITECTURE-BLUEPRINT.md`, `BUILD-PLAN.md` (Slices 0–6), ADR-001  

**Missing vs README promises:** schemas/, many docs scripts, full lifecycle, Drive write/readback, Temporal/OPA/Postgres stack.

**PR:** https://github.com/empire-mind/pmps-docs/pull/1  

### D — Corpus / memory / ops

| Asset | Feeds |
|-------|--------|
| Librarian harvest | Gap analysis inputs (what files exist) |
| pmps-ai-memory | Vocabulary, skills, pending questions |
| pmps-core | Older enterprise structure & product intent |
| pmps-runbooks | How humans run finance/ops procedures |
| pmps-evidence | Signed/snapshot proof trail |

---

## 4. Where gap analysis and document design fit (clean)

```text
                 ┌─────────────────────────────┐
                 │  A. Control STANDARD        │
                 │  (register, gates, ISO)     │
                 │  Vault: Business Doc Ctrl   │
                 └──────────────┬──────────────┘
                                │ rules
     ┌──────────────────────────┼──────────────────────────┐
     v                          v                          v
┌─────────────┐         ┌───────────────┐          ┌────────────────┐
│ Librarian + │  gap    │ Gap analysis  │  missing │ B. DOCUMENT    │
│ Drive/SP/   │ ──────► │ (capability)  │ ───────► │ DESIGN         │
│ memory/core │ compare │ Slice 3 later │  docs    │ pmps-design-   │
│ corpus      │ to need │ + BDC matrix  │          │ system         │
└─────────────┘         └───────────────┘          └───────┬────────┘
                                                           │ draft + brand
                                                           v
                                                ┌────────────────────┐
                                                │ C. CONTROL PLANE   │
                                                │ pmps-docs engine   │
                                                │ intake→approve→    │
                                                │ issue + ledger     │
                                                └─────────┬──────────┘
                                                          v
                                                Controlled master (Drive)
```

| Capability | Today (PROVEN) | Target |
|------------|----------------|--------|
| **Document design** | `pmps-design-system` skill + validator | Tagged releases; installed hash readback |
| **Gap analysis** | Manual: BDC matrix + `document-library.yaml` statuses (`GAP`/`FOUND`/…) + Librarian inventory | Automated Slice 3 `gap_finding` from corpus + obligations |
| **Control/issue** | Mini engine off-main; Drive IDs in config only | main merged; lifecycle + readback |

---

## 5. Contradictions to clean (trust debt)

| Conflict | Resolution |
|----------|------------|
| ATLAS: pmps-docs empty · branch has V1 | Treat **main** as empty until PR #1 merges; ATLAS needs refresh after merge |
| pmps-core “canonical enterprise” vs design-system + BDC pack | **Split authority:** core = business/product canon; design-system = brand/design; BDC pack = control standard; pmps-docs = automation |
| Session notes claiming golden-path 9-stage / commit 0014b6d | **Not on GitHub remote** — discard as non-evidence |
| Multiple “100/100 green” claims (finance OS, etc.) | Out of band; do not inherit into Foundations status |
| SharePoint gates vs Google Drive filing in pmps-docs config | **Decide storage end-state** (Google-primary post-migration vs dual) before bulk control build |
| Linear Ashley pilot vs Session Control design (2026-07-28) | Pilot is one track; session-control project is separate governance design (implementation pending) |

---

## 6. Single status labels (use these going forward)

| Label | Meaning |
|-------|---------|
| **EMPTY** | Default branch has no product content |
| **STUB** | Runnable thin slice, not product-complete |
| **DRAFT** | Written design/pack, not commissioned |
| **LIVE-PARTIAL** | Used in anger with known gaps |
| **BLOCKED** | Needs auth, human gate, or missing dependency |
| **PROVEN** | Re-runnable evidence this period |

**Program roll-up:** **LIVE-PARTIAL / fragmented** — strong design-system stub+tests; control standard on paper; control plane not on main; gap analysis manual only; no single commissioned pipeline.
