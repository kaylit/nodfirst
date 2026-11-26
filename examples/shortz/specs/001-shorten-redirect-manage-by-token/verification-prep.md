# Verification prep — production smoke (T26)

Fill this after the human deploys to Vercel Hobby. Used later by `/nodfirst-verify`.

- **Production URL:** https://production-host.example/
- **Deployed at (UTC/local):** 26/11/2026 ~21:29 UTC / 22:29 CET
- **Checked by:** agent (browser + HTTP checks); deploy owned by Luca Lanzano
- **Date:** 26/11/2026

## Smoke checklist

| # | Step | Pass? | Notes |
|---|---|---|---|
| 1 | Create short link on `/` | [x] | Result showed short link, new management token, copy/download, recovery warning |
| 2 | Open short link → original URL | [x] | `GET /r/…` → 302 `https://example.com/prod-smoke-001` |
| 3 | Manage: unlock with token → link listed | [x] | List showed short link, destination, created time |
| 4 | Delete link → short URL no longer redirects to original | [x] | Confirm delete; list empty; `GET /r/…` → 302 `/link-not-found` |
| 5 | `/privacy` loads | [x] | HTTP 200 |

## Result

- [x] All five steps passed on production
- Blockers / follow-ups: _none_
