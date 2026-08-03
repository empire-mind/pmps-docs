# Google Drive — Foundations Controlled Workspace

**ID:** `PMPS-STD-GOV-DRIVE-001`  
**Purpose:** One clean place for **approved** and **in-control** documents.  
**Primary storage decision:** **Google Drive** (not SharePoint) for new controlled masters.

---

## 1. Existing IDs (from control-room config — verify live)

| Item | ID | Notes |
|------|-----|--------|
| Shared Drive | `0AGC3u-mEfahxUk9PVA` | Confirm name in UI |
| Foundations root | `1Q1TeUT7T0v_8u6UgXA_pmKpebCifo7w5` | Confirm |
| Master register (declared) | `1rCAQ4kZDK6YPbH_LBkX4duGTyShYVYQo` | Confirm or recreate |
| Catalog (declared) | `1sMxpaWfVrO2EQJX4QYq8owfFoCWcTLlv` | Optional |
| Intake folder | `1EbA6SR73GeIOe9DmTAuWPCy9o7pFAFjU` | `99 INTAKE` |

**Action:** Eli opens each ID once; if broken, recreate under Shared Drive and update `config/control-room.yaml` + this doc in the same PR.

---

## 2. Create a **clean** Controlled Workspace (recommended layout)

If the existing Foundations tree is messy, create a **new sibling** folder (do not delete old yet):

```text
[Shared Drive] Premium Mobile Plant Solutions
└── PMPS Foundations Controlled Workspace     ← NEW clean root (name exact)
    ├── 00 START HERE
    │   ├── READ-ME-FIRST.md (export of CANON one-pager)
    │   ├── HUMAN-SOP.pdf (issued)
    │   └── LINKS.txt (Register, Notion, Linear, GitHub)
    ├── 01 CONTROLLED MASTERS                 ← only ACTIVE_CANONICAL files
    │   ├── 01 GROWTH
    │   ├── 02 WORKFORCE
    │   ├── 03 OPERATIONS
    │   ├── 04 FINANCE                        ← procedures only, no bank exports
    │   ├── 05 ENABLEMENT
    │   ├── 06 CLIENTS-PROJECTS
    │   └── 09 GOVERNANCE
    │       ├── Master-Document-Register.xlsx  ← SoT for identity/status
    │       ├── Approval-Receipts/
    │       ├── Standards/
    │       └── Gap-Register.xlsx
    ├── 02 DRAFTS-IN-PROGRESS                 ← optional; or use only 99 INTAKE
    ├── 90 RESTRICTED                         ← disabled until Eli access test
    ├── 95 EXTERNAL-EXCHANGE                  ← disabled until sharing test
    ├── 98 SUPERSEDED-ARCHIVE                 ← old versions (read-only)
    └── 99 INTAKE                             ← single landing zone for new files
```

**Rules:**

1. **01 CONTROLLED MASTERS** = only files with Register status ACTIVE_CANONICAL.  
2. **99 INTAKE** = only entry for new/untrusted files.  
3. Depth ≤ 2 under masters.  
4. No personal Desktop sync as authority.  
5. Naming: `PMPS-<TYPE>-<DOMAIN>-<NNN>_v<major.minor>_<short-title>.pdf`  
6. When v1.1 issued, move v1.0 to **98 SUPERSEDED-ARCHIVE** and update Register.

---

## 3. Separate “project” for cleanliness

Treat **“PMPS Foundations Controlled Workspace”** as its own Drive project:

- Distinct from general company dump folders  
- Distinct from SaaS/product engineering drives  
- Share only to Ashley, Eli, and named controllers  
- External sharing **off** by default  

Legacy Foundations / OneDrive / SharePoint trees become **read-only discovery sources** until migrated row-by-row via Register.

---

## 4. Master Document Register (Sheet)

Minimum columns (from BDC schema + hash):

`document_id | document_title | department | document_type | status | current_version | sha256 | canonical_location | owner | approver | effective_date | review_due_date | supersedes | sensitivity | notion_page_id | linear_issue | notes`

Statuses allowed:

- `DRAFT`  
- `UNDER_REVIEW`  
- `ACTIVE_CANONICAL`  
- `SUPERSEDED_DO_NOT_USE`  
- `BLOCKED_SOURCE_MISSING`  
- `LEGAL_REVIEW_REQUIRED`  

---

## 5. Human setup checklist

- [ ] Shared Drive accessible  
- [ ] Controlled Workspace root created  
- [ ] START HERE contains links  
- [ ] Register sheet created + one sample row  
- [ ] 99 INTAKE empty or only known drafts  
- [ ] Old trees labelled `LEGACY — DO NOT USE AS OFFICIAL` in folder description  
- [ ] control-room.yaml IDs updated if recreated  
- [ ] Notion + Linear links pasted in START HERE  

**Revision:** 2026-08-03.r1
