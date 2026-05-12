#!/usr/bin/env python3
import os
import sys

STEP = 24
EXPECTED_ARTIFACT = 'rules/security-rules.yml'
REQUIRED_MARKERS = ['rules:', 'id: insecure-eval', 'message:', 'severity: ERROR', 'pattern: eval($X)']


def main():
    errors = []

    if not os.path.exists(EXPECTED_ARTIFACT):
        errors.append(f'Artifact not found: {EXPECTED_ARTIFACT}')
    else:
        with open(EXPECTED_ARTIFACT, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        for marker in REQUIRED_MARKERS:
            if marker not in content:
                errors.append(f'Missing marker in {EXPECTED_ARTIFACT}: {marker}')

    if errors:
        print('STEP VALIDATION FAILED')
        for err in errors:
            print(f'- {err}')
        return 1

    print(f'STEP {STEP} VALID')
    return 0


if __name__ == '__main__':
    sys.exit(main())
