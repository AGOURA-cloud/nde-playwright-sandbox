# GitHub + official Playwright smoke test

Isolated research-only branch. The fixture is synthetic, with no credentials, production services, or NOVA/AGOURA changes.

Workflow installs pinned @playwright/test and its Chromium browser on an ephemeral GitHub-hosted Ubuntu runner, runs the smoke test, and uploads a trace on failure.

Acceptance: launch Chromium, open local fixture, Add alpha => Items: 1, Reset => Items: 0. This is **GitHub Actions + Playwright Test**, not a direct ChatGPT MCP connection or Codex-to-Playwright MCP invocation.

A green GitHub Actions job is required before claiming runtime success. GitHub Actions minutes may count toward repository billing/allowance.
