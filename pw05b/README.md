# PW-05B — Dockerless isolation research (NOVA development tooling)

**Status: research and non-destructive capability probe prepared. NOT CONNECTED TO PLAYWRIGHT.**

Purpose: help the assistant build and test NOVA, **not** deploy Playwright into the NOVA trading engine.

## Preserved verified history

- PW-03: https://github.com/AGOURA-cloud/nde-playwright-sandbox/actions/runs/45062362778 — isolated Docker Playwright MCP synthetic browser verified. This did **not** prove an authenticated Codex agent invoked Playwright.
- PW-04: https://github.com/AGOURA-cloud/nde-playwright-sandbox/actions/runs/45063081659 — Codex CLI authentication gate: `NO_AUTH` on GitHub Actions.
- PW-05: Work report supplied by the user — Codex CLI reported ChatGPT authentication, but Docker socket access failed with permission denied and the Work provider reported unrestricted network policy. No browser was started. The Work report is context from the user, not independently retested here.

## Official research findings

1. Dockerless OS-enforced Linux sandboxing is possible on **supported hosts** through bubblewrap/user/network namespaces. OpenAI documents that Codex's sandbox uses bubblewrap and may refuse to run if the platform cannot enforce a requested permission policy.
2. OpenAI also documents wrapping a local MCP server with `codex sandbox --permission-profile ...`, with its dependencies prepared *before* network access is disabled. **This is a conditional architecture pattern, not proof it works in ChatGPT Work Cloud.** Verify the installed Codex CLI version's actual syntax before using it.
3. Microsoft's Playwright `--isolated` only creates a temporary browser profile. Its origin allow/block options are explicitly **not** security boundaries. `--no-sandbox` weakens security and must not be used.
4. An authenticated Codex CLI does not prove a safe MCP browser process, and a successful namespace probe does not prove filesystem restrictions, process restrictions, secret isolation, or no egress.

Sources:
- https://openai.com/index/inside-the-codex-sandbox/
- https://learn.chatgpt.com/docs/sandboxing
- https://learn.chatgpt.com/docs/permissions
- https://github.com/microsoft/playwright-mcp

## Safe capability check in the existing Work session (no browser)

Use the exact `research/pw05b-dockerless-isolation` branch:

```bash
python3 -m unittest discover -s pw05b -p 'test_*.py' -v
python3 pw05b/probe.py
codex sandbox --help
```

The first two commands have no internet requests, credentials or browser execution. The third only prints available CLI options. The Python probe tries to create a new **empty, unprivileged network namespace** using `unshare`; it does not open a network socket. This may fail because the cloud platform disallows user namespaces. That is an expected *blocker*, not a bug. The probe deliberately never reports full isolation as verified.

Interpret statuses:
- `BLOCKED_OR_UNVERIFIED` or `NOT_ISOLATED`: STOP. Do not start Playwright MCP.
- `NETWORK_NAMESPACE_CREATED_ONLY`: STOP and review; additional runtime proof of filesystem constraints, outbound isolation, available browser dependencies, and sanitized agent-driven MCP trace is mandatory before browser execution.

Never modify system sysctls, container privileges, network policy, paid services, credentials, private repositories, or NOVA/AGOURA production. Do not install dependencies or try `--no-sandbox` to bypass a failed check.

## Fallback if Work cannot enforce this security boundary

Use the **existing isolated GitHub Actions Playwright test runner** for reproducible browser regression checks, and let ChatGPT/Work inspect its test results and assist with code fixes. This gives automated browser testing without claiming live Playwright MCP tools are connected to Work. If a separate agent-driven connection becomes necessary, do it only in a verified, explicitly authorized sandbox. Work's own built-in Cloud Browser, where available, is a separate browser automation capability; it is not Playwright MCP.

**No live agent/Playwright integration was established by PW-05B research.**
