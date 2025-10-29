#!/usr/bin/env python3
import json, sys, pandas as pd, os

def parse_trivy(file_path):
    with open(file_path) as f:
        data = json.load(f)
    rows = []
    for r in data.get("Results", []):
        for v in r.get("Vulnerabilities", []) or []:
            rows.append({
                "Target": r.get("Target"),
                "VulnerabilityID": v.get("VulnerabilityID"),
                "Severity": v.get("Severity"),
                "PkgName": v.get("PkgName"),
                "InstalledVersion": v.get("InstalledVersion"),
                "FixedVersion": v.get("FixedVersion"),
                "CVSS": v.get("CVSS", {}).get("nvd", {}).get("V3Score", None)
            })
    df = pd.DataFrame(rows)
    out_path = os.path.join("data", "parsed_trivy.csv")
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} vulnerabilities to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_trivy.py <trivy.json>")
        sys.exit(1)
    parse_trivy(sys.argv[1])
