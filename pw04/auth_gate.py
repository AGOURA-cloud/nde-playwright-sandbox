"""Fail-closed, read-only Codex authentication preflight.

Never prints credential data. No sign-in, model requests, or network calls.
"""
from __future__ import annotations
import subprocess


def classify(exit_code: int, output: str) -> str:
    normalized = " ".join(output.lower().split())
    if "not logged in" in normalized or "not authenticated" in normalized:
        return "NO_AUTH"
    if exit_code == 0 and ("logged in using chatgpt" in normalized or "logged in using an api key" in normalized or "logged in using api key" in normalized):
        return "AUTH_PRESENT_NOT_APPROVED"
    return "INDETERMINATE"


def main() -> int:
    try:
        result = subprocess.run(
            ["codex", "login", "status"], text=True, capture_output=True,
            timeout=15, check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        print("PW04_AUTH_GATE=INDETERMINATE")
        return 2
    status = classify(result.returncode, result.stdout + "\n" + result.stderr)
    print("PW04_AUTH_GATE=" + status)
    # A configured account never authorizes a run automatically.
    if status == "NO_AUTH":
        return 0
    if status == "AUTH_PRESENT_NOT_APPROVED":
        return 3
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
