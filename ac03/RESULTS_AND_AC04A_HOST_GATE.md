# AC-03 Results and AC-04A Codex Cloud Host Gate
Date: 2026-11-23. Source: user-provided Work audit; raw Work session logs not independently retrieved here.

## AC-03 verified/reported
- Official Codex CLI supports local stdio and Streamable HTTP MCP; Secure MCP Tunnel is documented as a ChatGPT-to-private-MCP route, not an existing configured connection.
- Current Work session had no callable Playwright MCP, no configured secret bindings or outbound identities, and no verified private HTTP preview; one SSH portal reported.
- Codex CLI 0.172.0-alpha.2 supports command or URL. Chromium on PATH. Tunnel-client and playwright-mcp commands absent. Existing Work sandbox restrictions persist. Codex stdio MCP server sandbox confinement is not automatic.
- Collaboration-pilot Codex Cloud environment was previously created; runtime inventory, attachment, confinement, allowance, and private preview remain unverified.
- GitHub Actions previously demonstrated isolated standalone MCP browser interaction, not authenticated Codex-to-MCP or interactive preview.
- Codespaces listing attempt failed at shell proxy before GitHub response; availability/allowance unknown.
- ChatGPT custom MCP and tunnel permissions may require workspace tier, admin/owner, Platform organization roles and tunnel association. User's eligibility not established. No tunnel created.
- AC-02 was treated as completed, but no separate named evidence artifact located in the two research repositories.
- No costs, credentials, installs, hosting, tunnel, security changes, production changes or trading were initiated.

## Recommendation
**AC-04A: read-only verification of the existing collaboration-pilot Codex Cloud executor first.** No installation or MCP/browser launch yet.

1. Verify registered environment identity and whether the existing authenticated Codex session can attach to it through officially supported mechanisms.
2. Inspect available runtime and allowance (if visible), browser/Chromium availability, child-process isolation policy, and whether a private HTTP preview is supported.
3. Confirm a browser process could be confined from production secrets, host sockets, unrelated repositories, and unrestricted network access. Do not treat `--isolated` browser profile as a security boundary.
4. Identify whether local MCP stdio launch is supported by this executor and what approved configuration/permissions would be needed.
5. Classify each finding: OBSERVED, DOCUMENTED_UNVERIFIED, BLOCKED, or APPROVAL_REQUIRED.
6. If all preconditions pass, **stop and request user approval** before installing, starting services, or running the disposable end-to-end browser test.

## Proposed later AC-04B (requires separate approval)
In an authorized disposable host: run pinned Microsoft Playwright MCP and sandboxed Chromium beside private HTTP fixture; record actual Codex agent-to-MCP tool calls; click Add, observe `Items: 2`; edit scratch source; reload and verify `Items: 1`; Reset and verify `Items: 0`. Sanitize traces, clean up. Only after host loop passes consider Work-to-host Secure MCP Tunnel, subject to account and workspace permissions.

## Hard limits
No paid service or new credentials, privilege escalation, security bypass, persistent/public deployment, production NOVA or AGOURA modifications, live trading, or unapproved installations.

## Evidence integrity
This is a summary checkpoint of the user-supplied AC-03 report, not an independent recreation of its source citations or execution logs.
