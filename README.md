# EZSport EPG daily sync (GitHub free pilot)

## Setup
1. Create a **public** GitHub repository for the EPG distribution. Upload the contents of this ZIP to the repository root (including `.github/workflows/daily-epg.yml`). Do not commit the source EPG URL or credentials.
2. Repository Settings → Secrets and variables → Actions → New repository secret. Name: `EPG_SOURCE_URL`; value: your original XMLTV URL.
3. Repository Settings → Actions → General → Workflow permissions → **Read and write permissions** (if configurable). Workflow also requests `contents: write`.
4. Actions → Daily EPG → Run workflow. Wait for success.
5. The resulting fixed download URL is `https://github.com/OWNER/REPO/releases/download/epg-latest/epg.xml.gz` (replace OWNER and REPO).
6. Verify the URL downloads a gzip file. EZSport must support XMLTV gzip, or decompress before parsing.

## Notes
- Scheduled time: 19:30 UTC = 02:30 Vietnam time the following day. GitHub scheduled jobs can be delayed or skipped.
- A public repository and release means the EPG data is publicly downloadable. Do this **only if the source license explicitly permits redistribution**. For a personal Open-EPG URL, ask for permission first.
- Github Releases is a pilot delivery mechanism, **not a guaranteed CDN**. Repeated release asset replacement can be affected by caching; app should revalidate/download with appropriate cache strategy.
- Public repository GitHub Actions scheduled jobs are subject to inactivity disabling and other GitHub limits. Monitor the workflow.
- The workflow validates XMLTV and retains the previous asset on failed validation.
- If the data must stay private, don't use a public release URL. A private repository release cannot be downloaded anonymously by the app without a token, and tokens must not be embedded in APKs.
