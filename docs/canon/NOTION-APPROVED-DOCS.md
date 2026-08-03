# Notion — Approved Documents List

**ID:** `PMPS-STD-GOV-NOTION-001`  
**Role:** Human-friendly **projection** of the Master Document Register  
**Not:** Source of truth for file bytes or approval  

---

## 1. Existing related Notion pages (discovered 2026-08-03)

| Page | URL | Role after canon |
|------|-----|------------------|
| PMPS Controlled Document Library & Gap Register — 2026-08-01 | https://app.notion.com/p/PMPS-Controlled-Document-Library-Gap-Register-2026-08-01-3aff792baa1381f48fa3d54786f39a70 | **Migrate content into** Approved Docs DB + Gap view; then mark header “SUPERSEDED by Canon” |
| PMPS Business Foundations Pilot — Ashley | https://app.notion.com/p/PMPS-Business-Foundations-Pilot-Ashley-3aff792baa1381068e0def0b4c51ea83 | Delivery notes only |
| PMPS Automation Portfolio Control Room | parent of pilot DB | Keep; link Canon |
| PMPS Hermes Cloud Design Register | separate Hermes track | Do not mix |

---

## 2. Create database: **PMPS Approved Documents**

**Parent:** Automation Portfolio Control Room (or PMPS hub page)  
**Title property:** Document Title  

| Property | Type | Notes |
|----------|------|--------|
| Document ID | Title or Rich text (unique) | PMPS-… |
| Status | Select | ACTIVE_CANONICAL, SUPERSEDED_DO_NOT_USE, UNDER_REVIEW, DRAFT (DRAFT optional hide) |
| Version | Text | |
| SHA-256 | Text | |
| Drive link | URL | canonical_location |
| Department | Select | |
| Type | Select | SOP, Policy, Standard, Register, Form, Checklist… |
| Owner | Person | |
| Approver | Person | |
| Effective | Date | |
| Review due | Date | |
| Sensitivity | Select | |
| Linear | URL | |
| Git evidence | URL | optional |
| Notes | Text | |

**Views:**

1. **Official only** — filter Status = ACTIVE_CANONICAL  
2. **Due for review** — review due within 30 days  
3. **Superseded**  
4. **By department** board/table  

**Sync rule:**  
- Register changes first → Notion updated same day  
- If Notion and Register disagree → **Register wins**; fix Notion  

---

## 3. Canon pointer page (required)

Create page **PMPS Foundations — CANON (start here)** with:

1. Link to GitHub `docs/canon/CANON.md`  
2. Link to Drive Controlled Workspace  
3. Link to Master Document Register  
4. Link to this Approved Documents DB  
5. Link to Linear Foundations project  
6. One paragraph: “Obsidian mirrors this; chat is not SoT.”

---

## 4. What never goes in Notion as authority

- Full payroll/HR files  
- Signed contract PDFs as only copy  
- Secrets  
- Claiming APPROVED without SHA-256  

**Revision:** 2026-08-03.r1
