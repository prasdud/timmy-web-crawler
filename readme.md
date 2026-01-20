# Timmy 🕷️

Timmy is a simple web crawler written in Python.

It can crawl a given domain and discover:
- Subdomains  
- Pages  
- Files hosted on the domain  

This project is intended **purely for educational purposes**.

---
## Deprecated, Dev Note

This was the first actual thing i built. Proud of it. However not working on it anymore.
---

## Features

- Domain crawling
- Subdomain discovery
- Forward and backward parsing
- Optional output buffering to an external file
- Time-limited execution (run for *n* seconds)
- Multithreaded crawling

---

## Usage Notes

- When crawling YouTube, use:

https://youtube.com

**Do not** include a trailing slash:

https://youtube.com/

This causes an error.

---

## Development History

### 15-07-2024
- **Major refactor**
- Cleaned up the entire codebase
- Broke logic into smaller functions
- Active development moved to the `develop` branch

---

### 16-07-2024
- SSL certificate issue no longer occurs  
- No explicit fix was applied  
- Unclear why it now works, but it does

---

### 24-07-2024
- Added forward and backward parsers
- Added output buffering to external files
- Added time flag (crawler runs for a fixed number of seconds)
- Introduced threading

---

## Known Issues (Historical)

During early development, SSL-related errors occurred:

[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
unable to get local issuer certificate (_ssl.c:997)

OSError: Could not find a suitable TLS CA certificate bundle,
invalid path: ca_bundle.crt


The crawler failed on sites whose certificates were not trusted by all browsers, based on checks from sslshopper.com.  
This issue no longer appears as of 16-07-2024.

---

## Current State

The codebase is **messy and ugly**, but functional.  
Refactoring is intentionally paused to avoid breaking working behavior.

Even the author is currently confused by the execution flow.

---

## Planned Cleanup

- Draw a full execution flowchart
- Map out crawler logic end-to-end
- Split logic into proper modules
- Perform a controlled refactor
- Merge into `main` branch after cleanup

---

## Goals

- Once external links are discovered, recursively crawl each of them

---

## TODO

- Color-code different file types (questionable usefulness)
