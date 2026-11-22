# NOVA development tooling — PW-03 isolated Codex MCP preflight

## Status: OFFLINE CI PREFLIGHT PASSED — NOT CONNECTED TO CHATGPT

Research-only: the purpose is to help the assistant build/test NOVA, **not** to add Playwright to NOVA's trading system. PW-01 research and PW-02 isolated browser/MCP tests were previously done on `research/pw-mcp-once`. This branch retains that workflow unchanged.

This checkpoint adds an **inert** example Codex configuration (`enabled = false`), without credentials, public endpoints, host filesystem mounts or exposed ports. The pinned Docker image is nonroot, with no network, dropped Linux capabilities and a disposable browser profile. It can exercise synthetic pages only, not remote websites.

### Why this does not complete PW-03

Passing the original 15/15 GitHub Actions synthetic assertions proves the isolated MCP server/protocol and basic browser interactions, **not** that ChatGPT or Codex Cloud can call it. Playwright is not a directly connected tool in our ChatGPT conversation. The selected Codex environment must separately support Docker / a safe executor and successfully discover the MCP tools. Custom ChatGPT MCP connections have plan/workspace requirements and connect through a remote HTTPS server or secure tunnel; GitHub Actions is not itself a persistent MCP endpoint.

### Safe next test in a trusted Codex executor

1. Verify that the executor supports the desired Codex MCP settings and Docker, and has the pinned image available. **Do not pull/install/upgrade images, expose secrets, or spend money without separately approved limits.**
2. Review `codex-playwright-offline.example.toml`. Keep `--network none`, nonroot, no mounts/ports, and `default_tools_approval_mode = "prompt"`.
3. Only after the local preflight, place a reviewed copy in the trusted project's `.codex/config.toml` or user config, and explicitly turn `enabled = true` for a synthetic-only test.
4. Run `codex mcp list`, initialize/discover the server's tools, and prove that **the development agent** can navigate a synthetic page, click, snapshot, read its DOM, screenshot and close. Capture sanitized evidence.
5. Stop before accessing real sites or accounts. Do not modify NOVA, TradingView, Cloudflare, Binance, credentials or live trading.

### Static check

Run `python3 check_config.py` from this directory (Python 3.11+). This checks the inert example, not live MCP communication.

References: `microsoft/playwright-mcp` and OpenAI's official Codex MCP documentation.


## Verified one-time CI preflight (2026-11-22 UTC)

**Result: PASS** — https://github.com/AGOURA-cloud/nde-playwright-sandbox/actions/runs/45062362778

- GitHub Actions Ubuntu 24.04 Docker runtime and pinned Playwright MCP image: PASS
- Disconnected synthetic container: no network, mounts, ports, privileges, or root user: PASS
- OpenAI Codex CLI 0.171.0 installed on disposable runner: PASS
- `codex mcp list` and `codex mcp get playwright_offline` with locally enabled config: PASS
- Direct MCP JSON-RPC initialization and tool discovery: PASS
- Synthetic data-URL navigation, browser click, DOM state, accessibility snapshot: PASS
- Browser close and removal of the isolated container: PASS
- No API keys, trading accounts, NOVA production or Cloudflare deployments used.

**Scope caveat:** `codex mcp list/get` validates CLI registration only. Browser interactions were executed by a standalone offline JSON-RPC probe, **not** by an authenticated Codex reasoning agent and **not** by this ChatGPT conversation. PW-03 runtime preflight is complete; actual agent-to-Playwright authorization/integration remains pending. The committed example remains `enabled = false`.

The previous failed CI runs revealed two *test harness assertion* defects (an uncommitted probe on the first run, then mistakenly matching the original data URL and neglecting Playwright's accessibility ref IDs). Both were corrected in this branch; no Playwright server or strategy logic was modified. The final run passed all steps.
