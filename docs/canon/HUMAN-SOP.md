# HUMAN SOP — PMPS Controlled Documents

**ID:** `PMPS-PRO-GOV-001`  
**Audience:** Ashley, Eli, anyone who creates or uses PMPS documents  
**Time to learn:** 10 minutes  

---

## A. Before you create or change a document

1. Check the **Master Document Register** (Drive → `09 GOVERNANCE & DOCUMENT CONTROL` → Register).  
2. If a row already exists for this topic → you are **revising**, not inventing a parallel doc.  
3. If nothing exists → you will create a **draft**, not an official doc yet.

## B. Drafting

1. Put working files only in:
   - Drive **`99 INTAKE`**, or  
   - a clearly named **DRAFT** subfolder — never overwrite ACTIVE masters in place.  
2. Use brand rules from **pmps-design-system** (colours, fonts, logo, controlled-doc header fields).  
3. Fill metadata: title, owner, approver, version, classification (Internal/Confidential/…).  
4. Do **not** put payroll/HR personal packs, signed contracts, or live finance extracts into chat tools or random folders.

## C. Getting it approved (mandatory)

Approver records **all** of:

| Field | Example |
|-------|---------|
| Decision | APPROVED / REJECTED |
| Document ID | PMPS-PRO-OPS-012 |
| Version | 1.0 |
| SHA-256 of final file | `abc123…` |
| Date/time | ISO |
| Name | Ashley Halvorson |

No hash → **not approved**.

## D. Issuing (making it official)

1. Copy/move the **exact** approved file into the correct Controlled Workspace folder (see DRIVE-WORKSPACE.md).  
2. Update Master Document Register:
   - status = `ACTIVE_CANONICAL`  
   - canonical_location = Drive link  
   - current_version + sha256  
   - effective_date  
3. Mark old version `SUPERSEDED_DO_NOT_USE` and set `superseded_by`.  
4. Update **Notion Approved Documents** list (same ID, link, version, hash).  
5. Close Linear task with links to Drive + Register row + Notion row.  
6. Obsidian: update mirror note only (pointer) — do not paste full controlled body if sensitive.

## E. Using documents day-to-day

1. Open from **Register** or **Notion Approved list** — not from email attachments or old Desktop copies.  
2. If someone sends a “new SOP” in chat → treat as draft until it completes C–D.  
3. Printed copies: mark “uncontrolled if printed” unless print-controlled process says otherwise.

## F. Weekly hygiene (15 min)

- [ ] Any file stuck in `99 INTAKE` > 7 days?  
- [ ] Any ACTIVE doc past `review_due_date`?  
- [ ] Notion list still matches Register (spot-check 5 rows)?  
- [ ] Linear Foundations project: blocked items have an owner?

## G. Never do this

| Don’t | Do instead |
|-------|------------|
| Save “final_v3_REAL” on Desktop as official | Issue via D |
| Edit ACTIVE master in place | New version → approve → supersede |
| Trust Notion over Drive | Drive bytes + Register win |
| Let AI “publish” without human hash sign-off | Human step C |
| Create a second Foundations folder tree | One Controlled Workspace only |
| Put secrets in Git/Obsidian/Notion body | Links + redacted metadata |

## H. Roles

| Role | Person | Does |
|------|--------|------|
| Operational owner | Ashley | Approves business content & visual OK |
| Technical owner | Eli | Drive structure, Git, automation, security |
| Document controller | Ashley until delegated | Register accuracy |
| Agents (Hermes etc.) | — | Draft, check, file *proposals* only |
