# PW-05C — One-batch Plan A + Plan B interactive development-loop evaluation

**Checkpoint status: test design and synthetic fixture prepared. Runtime tests inside ChatGPT Work: NOT YET RUN.**

Repository: `AGOURA-cloud/nde-playwright-sandbox`
Branch: `research/pw05c-parallel-capability-gate`

## Goal (not a generic Playwright smoke test)

Answer the user's single decision question for **each path**:

> Can the assistant independently **navigate, inspect, interact, debug and retest**, including changing a disposable local source file, **within one development session**?

A is Dockerless, agent-controlled Playwright MCP via the existing ChatGPT-authenticated Codex CLI in Work. B is Work's own Cloud Browser. Compare both in **the same Work task**, without repeating PW-03/PW-04/PW-05 and without conflating browser capability with source-code feedback-loop capability.

Prior checkpoint: `pw05b/README.md`, `pw05b/probe.py`, `pw05b/test_probe.py`.
Original pinned Docker config: `pw03/codex-playwright-offline.example.toml`.

## Shared acceptance criterion

For each path, record **five separate observable capabilities**:

1. **Navigate:** load the synthetic fixture or a supported public, credential-free test website.
2. **Inspect:** report visible DOM/state, screenshot or equivalent inspection evidence.
3. **Interact:** fill an input, click a button, observe the changed state.
4. **Debug:** detect a deliberate mismatch between expected and actual UI state, identify its source or explicitly say source inspection unavailable.
5. **Retest:** correct the **local throwaway source copy**, reload, and verify a passing assertion in the same Work session. Merely clicking again without changing code does **not** earn this check.

Record whether the **same agent/session** performed all steps, and whether a person had to take manual actions. Do not mark a path full PASS from a scripted standalone MCP client or one page screenshot.

### The fixture (local, disposable)

`pw05c/fixture.html` is self-contained, imports no external files and makes no requests. Expected test:

- Open the fixture in a browser.
- Enter `alpha`, click **Add item**.
- The list should have one `li` and the status should read **Items: 1**.
- One of those assertions is intentionally false in the original fixture.
- Inspect behavior first, then inspect **only the disposable fixture source**, diagnose and repair the defect **in an uncommitted temporary copy**, reload and retest successfully.
- Demonstrate another interaction by clicking **Reset** and observing `Items: 0`.

The fixture must not be committed as a fixed file; a temporary repaired copy is the evidence of debugging. Never touch NOVA/AGOURA code.

## Lane A — secure Dockerless Codex + Playwright MCP

**Security gate FIRST; never start MCP or browser until it is genuinely enforced.**

1. In the previously authenticated Work Codex environment, use only existing installed dependencies. Run:
   ```
   python3 -m unittest discover -s pw05b -p 'test_*.py' -v
   python3 pw05b/probe.py
   codex sandbox --help
   ```
   No model or browser launch is required for these commands; help is read-only. If the namespace probe returns `BLOCKED_OR_UNVERIFIED` or `NOT_ISOLATED`, record **A=BLOCKED**, do not launch a browser, and continue evaluating B in the same session.
2. Even if `NETWORK_NAMESPACE_CREATED_ONLY`, do **not** mistake it for isolation proof. Before enabling an MCP process, verify actual installed Codex version supports a server-specific permission profile, whether user/mount/network sandboxing can be enforced on **the MCP server process and its browser child**, and that the process has only an empty scratch workspace with no credentials, profile mounts, private repo mounts, or network egress. Do not bypass failing restrictions, use `--no-sandbox`, grant Docker privileges, change sysctls, install packages or weaken policies.
3. If a security gate cannot be conclusively proven, **stop Lane A there**. Log exact check, exit status and failure reason. If genuinely verified safe with preinstalled browser/MCP and within an existing subscription allowance, an agent-driven browser test may run against the local synthetic fixture. Capture sanitized evidence showing the authenticated agent's *actual MCP tool calls* (not merely a direct Python MCP client).
4. No new API keys, pay-as-you-go model requests, public MCP ports, credentials, network installations or secrets. Codex authentication alone does not meet the gate.

## Lane B — Work's own Cloud Browser

**Independent of Lane A's Docker/network failure. No local privileged commands needed.**

1. Within this SAME Work task, determine if a Work Cloud Browser tool is actually available and can independently navigate, inspect and interact on a supported public page. First preference is a **private built-in local preview** of the disposable `pw05c/fixture.html` *if the browser can open it without any public deployment, port exposure or permissions bypass*.
2. If no trusted private preview exists, do **not** publish anything. Use the publicly accessible, credentials-free official Playwright TodoMVC demo `https://demo.playwright.dev/todomvc/` for a **browser-interaction-only** test: create item `pw05c-alpha`, check status, toggle complete, delete item, and report observed evidence. Note the demo is external, so do not put private material in it.
3. A successful TodoMVC interaction proves navigation/inspection/interactivity only. It does **not** prove Work Cloud Browser can open a local development preview, inspect source, edit code and retest the modified project. If that bridge cannot be confirmed, label source-debug/retest **UNPROVEN**, not PASS.
4. If private local preview is available, run the shared synthetic failure/repair/retest workflow against the **temporary** copy. Record which tool performed browser actions and where source was edited. Keep user involvement zero except unavoidable permission prompts.

## One evidence table (required)

| Requirement | A: Dockerless Codex/Playwright MCP | B: Work Cloud Browser |
|---|---|---|
| Enforced acceptable isolation | PASS / FAIL / BLOCKED / UNPROVEN | Provider-managed; identify access constraints |
| Navigate | PASS / FAIL / BLOCKED / UNPROVEN | PASS / FAIL / BLOCKED / UNPROVEN |
| Inspect current UI state | ... | ... |
| Interact (input + click) | ... | ... |
| Debug intentional failure | ... | ... |
| Edit disposable source + retest | ... | ... |
| Same uninterrupted development session | ... | ... |
| Human help required | ... | ... |
| Evidence link / sanitized log | ... | ... |
| Final verdict | FULL LOOP / PARTIAL / BLOCKED | FULL LOOP / PARTIAL / BLOCKED |

Clearly distinguish **verified**, **reported by the user/Work provider**, and **inferred from documentation**. Give exact errors when blocked, propose the closest safe next experiment and do not claim success from documentation alone.

## Bounds

- Do **not** change or deploy NOVA, AGOURA, Cloudflare, TradingView, production, private repos or the real user account.
- Do **not** expose any source, local server, tokens, browser profile or ports publicly.
- Do **not** create credentials, paid calls, new subscriptions, scheduled jobs or API keys.
- Do not restart existing PW-03/04/05 workflows or repeat the same failed Docker check.
- GitHub research work remains isolated to this branch; don't create a new workflow or change default branch without separate review.
- If a path cannot satisfy the full development loop, preserve that limit in the verdict and continue with the other path *within the same batch*.

## Research documents used when creating this checkpoint

- ChatGPT Work Cloud Browser: https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt
- ChatGPT Work and Codex: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- Codex Linux sandbox mechanism: https://openai.com/index/inside-the-codex-sandbox/
- Microsoft Playwright MCP: https://github.com/microsoft/playwright-mcp

These explain potential capabilities, **not** that this particular Work instance has passed the gates.
