# Design 001: Shorten, redirect, manage by token

- **Spec:** `specs/001-shorten-redirect-manage-by-token/spec.md`
- **Status:** Approved

## 0. Sources

| # | Item (file or link) | Version or date read | Covers | Role |
|---|---|---|---|---|
| S1 | `specs/001-shorten-redirect-manage-by-token/spec.md` | Approved 26/11/2026 | Behaviour, named screens, states, English UI | authoritative (behaviour) |
| S2 | `project/profile.md` Section 7 | 26/11/2026 | Mobile-first, light theme, minimal UI, one job per screen | authoritative (visual constraints) |
| S3 | Human answers in design interview (tone, mobile priority, download) | 26/11/2026 | Visual intent defaults | authoritative (intent) |

**Reading of images** (confirmed by the human: N/A — no images provided)
- None.

**Design system:** `project/design-system.md` does not exist. No tokens invented here. Components below are **proposals** pending a design-system file or plan mapping. Light theme, mobile-first (~360 px first) per S2 and module web W3.

## 1. Flows

1. **Create without token** (US1, US3 · R1, R8)  
   Open Create → enter URL → submit → Creation result shows short link + new management token (copy, optional download) + recovery warning.

2. **Open short link** (US2 · R6, R7, R16)  
   Open short link → browser follows redirect to original URL, **or** Not found screen if missing/deleted. No management UI.

3. **Create with existing token** (US5 · R10)  
   Open Create → enter URL + paste management token → submit → Creation result shows short link and “added to your token” confirmation; **no** newly issued token.

4. **Manage: list, add, delete** (US4 · R12–R15)  
   Open Manage → enter token → see list → optionally add URL (same rules as create) → optionally delete with confirmation dialog → on confirm, link removed; opening that short link yields Not found.

## 2. Screens

### Screen: Create
- **Purpose:** Primary job — shorten a URL; optionally attach an existing management token.
- **Entry points:** App home / default landing; link “Shorten a URL” from Manage or Creation result.
- **Source:** S1 (spec §6) · S3 (Create is home)
- **Layout (smallest supported screen first):**  
  Top: product name **Shortz** (hero-level brand signal, not only a tiny nav word).  
  One short supporting line (`create.tagline`).  
  Field: Original URL (required).  
  Field: Management token (optional), visually secondary, collapsed or labeled as optional.  
  Primary button: Shorten.  
  Text link: Manage links → Manage.  
  No stats, promos, or secondary marketing blocks.
- **Larger screens:** Same single column, constrained readable width (content not stretched edge-to-edge on desktop); brand and form remain one composition.
- **Main actions:** Submit create; navigate to Manage; focus URL field on load.
- **Covers:** US1, US5 · R1–R5, R10–R11, R18–R19 · AC1–AC5, AC9–AC10, AC16

### Screen: Creation result
- **Purpose:** Show outcomes of a successful create; emphasise saving the token when newly issued.
- **Entry points:** After successful Create submit.
- **Source:** S1 · S3 (vertical stack; copy within thumb reach; download secondary)
- **Layout (smallest first):**  
  Brand name Shortz (smaller than Create hero is OK).  
  Heading: success.  
  Block: Short link + Copy.  
  **If new token issued:** Block: Management token (masked option MAY be proposed later; default show full token once) + Copy (primary) + Download (secondary) + warning callout (`result.tokenWarning`).  
  **If existing token used:** Confirmation that the link was added to that token; no new token block; link to Manage.  
  Actions: Shorten another; Manage links.
- **Larger screens:** Same stacked blocks in a narrow column.
- **Main actions:** Copy short link; copy token; download token (optional); go to Manage; create another.
- **Covers:** US1, US3, US5 · R8, R10, R18 · AC1, AC9

### Screen: Manage
- **Purpose:** Unlock with token, list links, add, delete.
- **Entry points:** “Manage links” from Create or Creation result; direct entry.
- **Source:** S1 · S3
- **Layout (smallest first):**  
  **Locked:** Brand; heading Manage links; token field; primary Unlock / View links; link back to Create.  
  **Unlocked:** Heading; short reminder that the token was accepted (do not re-display full token permanently on this screen by default — user already pasted it; optional “token in use” without revealing full value).  
  List: for each link — short link, original URL (wrap/truncate with expand), creation date/time, Delete control.  
  Add section: URL field + Add button (same validation as Create).  
  Link: Shorten on home (Create).  
  **Empty list:** English empty message + Add form still available.
- **Larger screens:** List can use two-line rows; still one column.
- **Main actions:** Submit token; add link; delete (opens confirm); leave to Create.
- **Covers:** US4 · R11–R15, R18–R19, R22 · AC10–AC14, AC16, AC19

### Screen: Delete confirmation (modal / dialog on Manage)
- **Purpose:** Explicit confirmation before permanent delete (R14).
- **Entry points:** Delete on a list row.
- **Source:** S1 (required confirmation) · proposed chrome
- **Layout:** Dialog over Manage: title, short explanation that the short link will stop working, Cancel (secondary), Delete permanently (destructive primary). Focus trapped in dialog; Escape = Cancel.
- **Larger screens:** Same dialog, centered.
- **Main actions:** Confirm delete; cancel.
- **Covers:** US4 · R14 · AC12, AC13

### Screen: Not found (short link)
- **Purpose:** Clear English not-found when short code missing or deleted; no redirect.
- **Entry points:** Opening unknown/deleted short link.
- **Source:** S1
- **Layout:** Brand; heading Not found; short body; link to Create (Shorten a URL). Same experience whether never existed or deleted (R7, R22 intent for short links).
- **Larger screens:** Same, narrow column.
- **Main actions:** Go to Create.
- **Covers:** US2 · R7 · AC7, AC8

### Screen: Server error
- **Purpose:** Safe generic failure (spec §6 / W10); no internal detail.
- **Entry points:** Unexpected server failure on any UI action.
- **Source:** S1 · proposed
- **Layout:** Brand; heading; body (`error.server`); control to try again or go to Create.
- **Main actions:** Retry / go home.
- **Covers:** Spec §6 generic server error · R18

### Non-screen: Redirect
- **Purpose:** Successful open of a short link leaves the app UI and lands on the original URL (R6). No branded interstitial required in v1.
- **Covers:** US2 · R6, R16 · AC6

## 3. States

| Screen / component | Empty | Loading | Error | Offline | Permission denied (if any) | Source (given / proposed) |
|---|---|---|---|---|---|---|
| Create | Empty URL + optional token; no result | Primary button busy/disabled; prevent double submit | Inline English errors (validation, invalid token, rate limit); preserve fields | English network failure message; no offline mode | N/A | S1 / proposed copy |
| Creation result | N/A (only after success) | N/A for initial paint | If copy/download fails: brief English feedback, token still visible | Same network message if a later action fails | N/A | S1 / proposed |
| Manage (locked) | Empty token field | Unlock busy | Invalid token / rate limit — same error class (R22) | Network failure message | N/A (no accounts) | S1 / proposed |
| Manage (unlocked list) | “No links yet” + add form | List or add/delete busy | Add validation; delete failure; rate limit | Network failure message | Actions without token refused → return locked with error | S1 / proposed |
| Delete confirmation | N/A | Confirm busy while deleting | Delete failed → message, dialog may stay open | Network failure | N/A | proposed |
| Not found | N/A (static) | N/A | N/A | N/A | N/A | S1 |
| Server error | N/A | N/A | Static safe message | N/A | N/A | S1 / proposed |

## 4. Components

| Component | Existing / New | Notes |
|-----------|----------------|-------|
| Page shell (brand + main) | New (proposal) | Light theme; mobile-first; no card-heavy dashboard |
| Text field | New (proposal) | Label, error text, optional hint; URL and token |
| Primary button | New (proposal) | Min touch target 44×44 CSS px |
| Secondary button / text button | New (proposal) | Copy, Download, Cancel, nav links |
| Destructive button | New (proposal) | Delete permanently |
| Inline error / alert | New (proposal) | Errors and token warning; not colour alone |
| Result field + Copy | New (proposal) | Short link and token display with copy |
| Download control | New (proposal) | Secondary next to token Copy |
| Link list + row | New (proposal) | Short link, original URL, date, delete |
| Confirm dialog | New (proposal) | Focus trap; Escape cancels |
| Nav text link | New (proposal) | Create ↔ Manage |

Implementation mapping to a component library is a **plan** concern (profile mentions shadcn); this design does not bind library names.

## 5. Copy (i18n)

Language: English (R18). Keys for a message catalogue (W4); no hard-coded strings in components at implement time.

| Key | Text | Context |
|-----|------|---------|
| `brand.name` | Shortz | Product name |
| `create.tagline` | Shorten a link to share anywhere. | Under brand on Create |
| `create.urlLabel` | Destination URL | URL field |
| `create.urlHint` | http or https only | Hint |
| `create.tokenLabel` | Management token (optional) | Optional token |
| `create.tokenHint` | Paste your token to add this link to your list. | Hint |
| `create.submit` | Shorten | Primary |
| `create.navManage` | Manage links | Link to Manage |
| `create.errorEmpty` | Enter a URL. | Validation |
| `create.errorInvalid` | Enter a valid http or https URL. | Validation / bad scheme |
| `create.errorTooLong` | That URL is too long. Use at most 2048 characters. | R5 |
| `create.errorToken` | That management token is not valid. | R11, R22 — same class always |
| `create.errorRateLimit` | Too many attempts. Try again later. | R19 |
| `create.errorOffline` | You appear to be offline. Check your connection and try again. | Network |
| `result.titleNew` | Your short link is ready | New token path |
| `result.titleAdded` | Link added to your list | Existing token path |
| `result.shortLinkLabel` | Short link | |
| `result.tokenLabel` | Management token | New token only |
| `result.tokenWarning` | Save this token now. If you lose it, you cannot recover it. Your short links will keep working. | R8, R9 |
| `result.copy` | Copy | |
| `result.copied` | Copied | Announcement / feedback |
| `result.download` | Download | Optional token download |
| `result.manage` | Manage links | |
| `result.another` | Shorten another | Back to Create |
| `manage.title` | Manage links | |
| `manage.tokenLabel` | Management token | Locked |
| `manage.unlock` | View links | |
| `manage.backCreate` | Shorten a URL | |
| `manage.empty` | No links yet. Add one below. | Empty list |
| `manage.colShort` | Short link | List |
| `manage.colOriginal` | Destination | List |
| `manage.colCreated` | Created | List |
| `manage.delete` | Delete | Row action |
| `manage.addLabel` | Destination URL | Add form |
| `manage.addSubmit` | Add link | |
| `manage.errorToken` | That management token is not valid. | Same class as create.errorToken |
| `manage.errorRateLimit` | Too many attempts. Try again later. | |
| `manage.errorOffline` | You appear to be offline. Check your connection and try again. | |
| `manage.deleteFailed` | Could not delete that link. Try again. | |
| `delete.title` | Delete this short link? | Dialog |
| `delete.body` | This cannot be undone. Anyone with the short link will see a not found page. | |
| `delete.confirm` | Delete permanently | |
| `delete.cancel` | Cancel | |
| `notFound.title` | Link not found | |
| `notFound.body` | This short link does not exist or is no longer available. | Same for never existed / deleted |
| `notFound.cta` | Shorten a URL | |
| `error.serverTitle` | Something went wrong | |
| `error.server` | Please try again. If the problem continues, try later. | No internals |
| `error.retry` | Try again | |

## 6. Accessibility

- **Keyboard order (Create):** brand/skip → tagline → URL → optional token → Shorten → Manage links.  
- **Creation result:** short link → Copy → (token → Copy → Download) → Manage → Shorten another.  
- **Manage locked:** token → View links → Shorten a URL.  
- **Manage unlocked:** add field → Add → list rows (short link, delete) → dialog when open.  
- **Focus:** Visible focus ring on all controls (W2). Dialog: focus trap; initial focus on Cancel or title; Escape cancels (AC13). After delete, focus returns to list or empty state.  
- **Labels:** Every field has a visible label (keys above); errors linked via `aria-describedby` / announced.  
- **Announcements:** Prefer polite live region for `result.copied`, form errors, and delete success; assertive for errors that block the task.  
- **Contrast:** Text and interactive elements meet WCAG 2.2 AA on light theme; token warning not by colour alone.  
- **Touch targets:** Primary controls ≥ 44×44 CSS px (W3).  
- **Motion:** Any feedback animation subtle; respect reduced motion.  
- **Zoom:** Layout usable at 200% text resize.  
- **Page titles:** Distinct English titles per screen (e.g. “Shorten a URL · Shortz”, “Manage links · Shortz”, “Link not found · Shortz”).

## 7. Conflicts, gaps and open questions

**Conflicts**
- None (no image sources to conflict with the spec).

**Gaps (all proposed; human to confirm)**
- [x] Full visual mockups — absent; layouts described in text only (proposed).
- [x] Whether token on Creation result is shown fully or partially masked — **proposed: show full token once** (easier to save; user must copy).
- [x] Whether Manage unlocked re-shows the full token — **proposed: do not** (reduce shoulder-surfing); token already provided to unlock.
- [x] Download file format/name — **deferred to plan** (e.g. plain text file); control exists in UI.
- [x] Exact light-theme colours/type — **no design-system tokens yet**; implement with profile + library defaults in plan, or run design-system playbook later.

**Open questions**
- [ ] Confirm proposed gaps above (masking, Manage token visibility, text-only design OK for approval).
- [ ] Browser/viewport matrix still profile D7 (plan); design assumes ~360 px min width mobile-first.

## 8. Approval

- Approved by: Luca Lanzano
- Date: 26/11/2026
