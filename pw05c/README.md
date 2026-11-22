# PW-05C — Dual-path interactive development-agent validation

**Status: controlled batch prepared; neither path yet proven end-to-end.**

## Mission
Evaluate **in the same Work session** whether an authorized development agent can navigate, click/type, inspect, diagnose, correct, and retest a synthetic UI, using:
- **A:** Codex CLI + Playwright MCP, only with verified OS-enforced Dockerless isolation.
- **B:** ChatGPT Work's native interactive Cloud Browser, where available. This is **not** Playwright MCP.

Both paths must meet the same evidence standard. Preserve all PW-03/04/05 history. Do not mistake standalone Playwright MCP tests or Codex login for agent-driven integration.

## Safe parallel research, then conditional tests

**A1 — no-browser preflight**: Read `pw05b/README.md`; run `python3 -m unittest discover -s pw05b -p 'test_*.py' -v`, `python3 pw05b/probe.py`, and `codex sandbox --help` (read-only). Confirm actual Work runtime supports enforcing outbound network isolation, filesystem restrictions, nonprivileged browser process, no credential mounts, and sandboxed MCP subprocess execution. A successful `unshare` result alone is not enough. If any boundary is unverified, mark **A=BLOCKED** and DO NOT start MCP/browser, bypass with `--no-sandbox`, alter sysctls, or install dependencies.

**B1 — native capability inventory**: In this same Work session, check whether Work exposes an **actual** Cloud Browser interactive capability (not just a description of it). Confirm whether the browser can visit a local synthetic page, perform clicks/typing, inspect DOM or screenshot, and continue in one session. If browser isn't available, mark **B=UNAVAILABLE**, not passed. Never try to obtain credentials or use private/production URLs.

**Synthetic UI (only after a path is approved to launch)**: use a disposable, entirely local synthetic HTML page with a textbox, submit button, status label and one intentional UI bug. The agent must (1) inspect the page, (2) type a test string, (3) click, (4) observe incorrect status, (5) identify and correct the synthetic bug in an isolated test fixture, (6) reload/retest and observe correct status, (7) capture sanitized action/observation trace. If native browser cannot open local synthetic content, use its supported synthetic `data:` or otherwise authorized isolated fixture; do not replace it with a public internet site without approval.

**A2 — only if A1 passes every isolation check**: Verify actual Codex CLI MCP registration and permitted browser process execution; capture sanitized `codex exec --json` evidence of agent-initiated MCP actions, not just a Python MCP client.

**B2 — only if B1 confirms native browser and safe synthetic fixture**: Run the same interactive development loop using Work's browser. Record whether browser interactions and code correction happened within the **same session**; distinguish UI-only changes from genuine code changes.

## Shared pass/fail rubric

| Criterion | A: Codex+MCP | B: Work Browser |
| --- | --- | --- |
| Enforced isolation and no sensitive access | UNTESTED | UNTESTED |
| Agent opens synthetic UI | UNTESTED | UNTESTED |
| Agent types and clicks | UNTESTED | UNTESTED |
| Agent inspects post-action state | UNTESTED | UNTESTED |
| Agent diagnoses synthetic bug | UNTESTED | UNTESTED |
| Agent corrects fixture code | UNTESTED | UNTESTED |
| Agent retests without user intervention | UNTESTED | UNTESTED |
| Sanitized evidence and cleanup | UNTESTED | UNTESTED |

Report each as PASS / BLOCKED / FAIL / UNAVAILABLE / UNTESTED with observed evidence, and recommend the best path. **Do not call a path integrated unless the full loop passes.**

## Non-negotiable scope
- Research repo: `AGOURA-cloud/nde-playwright-sandbox` only.
- No NOVA/AGOURA private files, production, trading, deployments, credentials, paid API requests, browser profiles, or unrelated sites.
- No weakening security settings or privilege escalation.
- Stop at any uncertain isolation boundary; do not treat the need to stop as failure of Playwright itself.

## References
- PW-05B: `pw05b/README.md`
- PW-04: `pw04/README.md`
- PW-03: `pw03/README.md`
