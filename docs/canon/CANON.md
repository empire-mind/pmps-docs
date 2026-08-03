# PMPS FOUNDATIONS — CANON (Single Source of Truth)

**Document ID:** `PMPS-STD-GOV-CANON-001`  
**Status:** ACTIVE_CANONICAL (program doctrine)  
**Effective:** 2026-08-03  
**Owners:** Ashley Halvorson (ops) · Eli Halvorson (tech)  
**Git home:** `empire-mind/pmps-docs` → `docs/canon/`  
**Rule:** If another note conflicts with this pack, **this pack wins**. Other notes become SUPERSEDED or REFERENCE ONLY.

---

## 1. One sentence

PMPS Foundations makes business documents **official**: one clean Drive home for approved files, one register of what’s approved, design that matches brand, delivery tracked in Linear, human-readable list in Notion, and Obsidian only mirrors the canon — never invents a second truth.

---

## 2. Authority map (memorise this)

| What | System of record | May project / copy |
|------|------------------|--------------------|
| **Approved file bytes** (PDF/DOCX masters) | **Google Drive** — Foundations Controlled Workspace | Nowhere else as “the” copy |
| **Which docs are approved** (identity, version, hash, status) | **Master Document Register** (Sheet in Drive Governance) | Notion Approved Docs list (read-only projection) |
| **How to design/brand docs** | **GitHub `pmps-design-system`** | Installed skill is a deploy, not SoT |
| **Automation, policy YAML, engine code** | **GitHub `pmps-docs`** | — |
| **Delivery roadmap & tasks** | **Linear** project *PMPS Foundations Program* | — |
| **Human portfolio / Ashley views** | **Notion** | Not allowed to override Drive/register |
| **Working memory / agent context** | **Obsidian** (ingest from canon) | Must link to canon IDs; no silent promotion |
| **Money / people systems** | Xero / JobAdder / TrackEasy | Never overridden by docs AI |

**Hard law:** *If it is not ACTIVE_CANONICAL in the Master Document Register, it is not an official PMPS document.*

---

## 3. What is NOT the source of truth

Treat as **reference / history / draft only** (do not run the business from these alone):

| Artifact | Why demoted |
|----------|-------------|
| Desktop “PMPS-Business-Foundations-Pilot” folders | Local workspace, not SoT |
| Linear issue text alone | Delivery tracker, not register |
| Notion pages that are not the Approved Docs DB | Portfolio / old digests |
| Chat / Hermes / Claude memory claims | Ephemeral |
| `pmps-core` April audit snapshot | Historical enterprise tree |
| SharePoint-as-default BDC “Next Gate 4” | **Superseded for storage primary** — Google Drive is primary controlled store (migration direction). SharePoint = legacy discovery source only until emptied |
| Session claims of “9-stage golden path proven / commit 0014b6d” | **False on GitHub remote** |
| Empty `main` scaffolds (`pmps-templates`, old empty `pmps-docs` main) | Not product |
| Finance OS “100/100” banners | Separate product claims |

---

## 4. The only happy path (human + system)

```text
1. WORK happens in drafts (99 INTAKE or personal draft)
2. DESIGN validated (pmps-design-system / brand rules) when branded output
3. HUMAN APPROVES exact file (name + version + SHA-256)
4. FILE lands in Drive Controlled Workspace (correct folder)
5. REGISTER row set ACTIVE_CANONICAL (hash + Drive link)
6. NOTION Approved Docs list updated (projection)
7. OBSIDIAN mirror note updated (pointer + summary only)
8. LINEAR task closed with evidence links
```

Nothing skips 3–5.

---

## 5. Pack contents (this folder)

| File | Purpose |
|------|---------|
| [CANON.md](./CANON.md) | This file — doctrine |
| [HUMAN-SOP.md](./HUMAN-SOP.md) | Day-to-day human procedure |
| [ROADMAP.md](./ROADMAP.md) | Phases to solid foundation |
| [DRIVE-WORKSPACE.md](./DRIVE-WORKSPACE.md) | Clean Drive project layout |
| [NOTION-APPROVED-DOCS.md](./NOTION-APPROVED-DOCS.md) | Notion list spec |
| [OBSIDIAN-INGEST.md](./OBSIDIAN-INGEST.md) | How Obsidian stays a mirror |
| [SUPERSEDED-INDEX.md](./SUPERSEDED-INDEX.md) | Old plans → status |
| [ANTI-CONFUSION.md](./ANTI-CONFUSION.md) | Rules so this never forks again |

---

## 6. Versioning of the canon itself

- Change only via PR to `pmps-docs`  
- Bump `document_id` revision in commit message  
- After merge: refresh Notion “Canon pointer” page + Obsidian mirror  

**Revision:** 2026-08-03.r1
