# PW-04 — Codex agent → Playwright MCP integration checkpoint

## Verdict: AUTHENTICATION BLOCKED (not an agent connection success)

**One-time CI gate passed**: https://github.com/AGOURA-cloud/nde-playwright-sandbox/actions/runs/45063081659

Confirmed using GitHub Actions Ubuntu runner:
- All six fail-closed authentication classifier tests passed.
- PW-03 inert config revalidated; the Playwright MCP entry remains **disabled by default**.
- Codex CLI `0.171.0` installed on the ephemeral runner; `codex mcp list/get` succeeded.
- `codex login status` yielded `PW04_AUTH_GATE=NO_AUTH`.
- `PW04_AGENT_EXECUTION=NOT_ATTEMPTED`; no actual Codex reasoning-agent ↔ Playwright MCP tool call was made.
- No API keys, OAuth tokens, model requests, external websites, live trading, or NOVA Cloudflare/GitHub production changes.

This is a *successful safety gate detecting an unmet prerequisite*, **not** proof of PW-04 integration.

PW-03 already proved synthetic Playwright MCP JSON-RPC navigation, click, DOM evaluation and snapshot from a standalone client in the same kind of isolated CI environment:
https://github.com/AGOURA-cloud/nde-playwright-sandbox/actions/runs/45062362778
PW-03's `codex mcp list/get` additionally proves Codex *registration*, but those browser interactions were performed by a separate Python test client rather than a signed-in Codex agent.

## Next authorized step (must be initiated through an appropriate Codex/Work environment)

Use the connected development project and a supported **authenticated Codex runtime**. Review `pw03/codex-playwright-offline.example.toml` and turn its disabled flag on only within a disposable environment after approving the experiment. Then verify **actual Codex agent tool invocations** on a synthetic HTML fixture, with read-only repository permissions and no production credentials, networked sites or browser mounts. Capture sanitized `codex exec --json` tool invocation evidence and result.

Do not copy tokens into chat, commit `~/.codex/auth.json`, or add a paid API key without explicit consent. For credential-based CI runs, consult the official `openai/codex-action@v1` security guidance: use GitHub secrets, not job-wide environment variables; API usage can incur charges. An authorized Codex-capable ChatGPT Work environment may provide an alternative, but its availability and permissions must be verified in that environment; this chat's MCP tool list does not expose Playwright or a Codex executor.

Source: OpenAI Codex docs (Non-interactive mode, authentication in CI) at https://learn.chatgpt.com/docs/non-interactive-mode.

## Preservation

- Sandbox branch only: `research/pw04-agent-integration-gate`
- Earlier PW-02 and PW-03 test workflows unchanged in meaning.
- No NOVA or AGOURA production code changed, no trading execution.
