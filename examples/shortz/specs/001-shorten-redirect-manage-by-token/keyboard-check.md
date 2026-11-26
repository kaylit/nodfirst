# Keyboard check — feature 001

- **Date:** 26/11/2026
- **Checked by:** agent (manual keyboard pass via Chromium Tab / Escape)
- **Scope:** Create (`/`), Manage locked (`/manage`), delete confirm dialog
- **Related:** design §6 focus; AC13 Escape = cancel

## Checklist

| Item | Result | Notes |
|---|---|---|
| Tab order — Create | Pass | Destination URL → Management token (optional) → Shorten → Manage links → Privacy |
| Tab order — Manage (locked) | Pass | Management token → View links → Shorten a URL → Privacy |
| Focus visible | Pass | Text inputs show a visible focus ring (`focus-visible` ring). Buttons use the same shadcn `focus-visible:ring` pattern. |
| Dialog Escape | Pass | Delete confirm closes on Escape; link remains (cancel behaviour). Cancel button still available afterward. |
| Dialog Cancel (pointer) | Pass | Covered by e2e AC13 (Cancel keeps link). |

## Out of scope / notes

- Next.js dev `nextjs-portal` may appear in Tab order in local `next dev` only; not present in production build.
- Unlocked Manage list / add form tab order follows the same labelled controls pattern; delete path verified for Escape as above.
