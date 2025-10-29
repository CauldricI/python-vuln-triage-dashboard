# python-vuln-triage-dashboard

A lightweight Python dashboard for triaging vulnerability data from multiple scanners (Trivy, Nessus, Prisma Cloud).

This project demonstrates how to normalize, merge, and visualize vulnerability results for prioritization using CVSS scores and severity.

## Features
- Parse and normalize JSON data from Trivy or Nessus
- Merge results into a single CSV or Pandas DataFrame
- Visualize top CVEs, affected packages, and severity distribution
- Export filtered results to CSV or dashboard widgets

## Quick Start
1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
