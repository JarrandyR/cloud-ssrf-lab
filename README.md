# Cloud SSRF Lab (Public → Internal Pivot)

This repository demonstrates a **Server-Side Request Forgery (SSRF)** vulnerability in a cloud-style architecture and shows how to properly remediate it.

## What This Lab Shows
- A public Flask app with a URL-fetch endpoint
- An internal-only service bound to `127.0.0.1`
- SSRF used to pivot from public → internal
- Mitigation that blocks loopback, private, and link-local destinations

## Architecture
See `architecture/diagram.txt`

## Exploit Example
/fetch?url=http://127.0.0.1:5001/internal/secret

markdown
Copy code

## Mitigation
- Resolve hostname server-side
- Block loopback and private IP ranges
- Return HTTP 403 for blocked destinations

## Why This Matters
SSRF vulnerabilities frequently lead to:
- Internal service exposure
- Cloud metadata access
- Credential leakage

## Disclaimer
For educational and authorized testing only.
