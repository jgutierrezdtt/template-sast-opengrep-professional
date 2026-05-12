#!/usr/bin/env python3
import json
import os
import sys

STEP = 4
EXPECTED_ARTIFACT = ".opengrep.yml"
EVIDENCE_FILE = ".tutorial/evidence/step-04.json"

def main():
    errors = []

    if not os.path.exists(EXPECTED_ARTIFACT):
        errors.append(f"Artifact not found: {EXPECTED_ARTIFACT}")

    if not os.path.exists(EVIDENCE_FILE):
        errors.append(f"Evidence file not found: {EVIDENCE_FILE}")
    else:
        try:
            with open(EVIDENCE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data.get("step") != STEP:
                errors.append(f"Invalid evidence step: expected {STEP}, got {data.get('step')}")
            if data.get("status") != "completed":
                errors.append("Evidence status must be 'completed'")
            if data.get("artifact") != EXPECTED_ARTIFACT:
                errors.append(f"Evidence artifact mismatch: expected {EXPECTED_ARTIFACT}")
        except Exception as exc:
            errors.append(f"Invalid JSON in evidence file: {exc}")

    if errors:
        print("STEP VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1

    print(f"STEP {STEP} VALID")
    return 0

if __name__ == "__main__":
    sys.exit(main())
