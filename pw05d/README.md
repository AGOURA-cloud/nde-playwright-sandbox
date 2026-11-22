# PW-05D — Isolate the missing editable-preview bridge (read-only planning checkpoint)

**Status: prepared, no PW-05D Work runtime test yet. No NOVA changes.**

## Evidence received from Work in PW-05C

- Plan A: authenticted Codex CLI available, but actual user/network namespace probe failed: `unshare: cannot open /proc/self/uid_map: Read-only file system`. The script classified `BLOCKED_OR_UNVERIFIED`. No MCP/browser launched.
- Plan B: Work Cloud Browser PASSED navigation, accessibility inspection and real interactive click/type/toggle/delete on credential-free React TodoMVC. The agent did so in the same session without human actions.
- Plan B local preview: binding a loopback server raised `PermissionError: [Errno 1] Operation not permitted`. Work couldn't open the synthetic scratch fixture. Thus the *source edit -> browser reload -> re-test* loop is NOT proven.
- The Work report states no paid calls, installations, deployments, credentials or production modifications. These are reported results, not tests independently replayed here.
- PW-05C checkpoint and fixture: `pw05c/README.md`, `pw05c/fixture.html`.

## Narrow goal for next Work session

**Do not re-run Plan A or public TodoMVC.** Find a safe platform-supported bridge from **editable throwaway source** to **the same Work agent's browser**. Evaluate these in a single batch and separately identify whether any approach is suited to private NOVA repo development.

### Read-only discovery checks (first)

1. Does Work expose a **native private preview** for a disposable local HTML artifact, without opening a socket, requiring Docker or publishing to the internet? Check available controls only; no setup or resource creation without authorization.
2. Can the Work Cloud Browser **directly open an ephemeral `data:text/html` URL** generated from a synthetic **scratch-only** HTML file using the supported navigation UI? Browser providers may block `data:` navigation; if so, record blocked and **do not evade**. This would be a *limited demonstration*, not a solution for a multi-file private web app.
3. Is **ChatGPT Sites private preview** available through the user's current Work surface? OpenAI documents creating, previewing and editing a site before publishing. **Discover access only**, do not create a persistent Site, publish, share or deploy it without separate explicit user approval. A Site-specific loop is not automatically the existing NOVA repo's loop.
4. Are there any **Codex Cloud preview** or first-party workspace preview controls already exposed to this session that allow an editable checkout and its interactive browser view, with no added costs or remote deployment? Inspect support and permissions read-only.

### If a fully ephemeral scratch-preview bridge works

Use `pw05c/fixture.html` copied to scratch; it intentionally contains an incorrect count.

- Navigate to the rendered original page (NOT a source text viewer).
- Enter `alpha`, click Add and record list-length 1 versus incorrect status `Items: 2`.
- Edit the **scratch copy of the HTML source** to correct count logic, not merely inject DOM changes or run a browser console command.
- Re-render or reload the changed source in the same browser session, Add `alpha` and confirm `Items: 1`; Reset then confirm `Items: 0`.
- State **what exact preview transport** permitted the code-to-browser step and whether it could scale to a private multi-file NOVA UI. Sanitized evidence only.
- Do not commit fixture fixes, modify real repositories, expose ports or credentials, alter permissions or launch paid services.

### If no ephemeral bridge is available

STOP and give precise blocker(s). Offer a **separate approval choice** for one non-public, disposable ChatGPT Site (if the feature is actually available); no creation until approved. Otherwise consider a preexisting Codex Cloud dev-preview environment if supported without setup. Never advise a public server, privilege elevation, security bypass or unrestricted remote browser connection as a substitute.

## Deliverable

One compact evidence matrix:
`Bridge candidate | accessible? | code edit and reload tested? | same agent/session? | works for private multi-file repo? | blockers | user approval required?`

Verdict must distinguish:
- **DIRECT_BROWSER_PASS** (already proven for Work, not Playwright MCP),
- **SYNTHETIC_EDIT_RETEST_PASS** (only if run and demonstrated),
- **NOVA_REPO_PREVIEW_PASS** (requires separate evidence against a dedicated private development preview),
- **MCP_AGENT_CALL_PASS** (not achieved).

## Documentation, not runtime proofs

- Cloud browser supports navigation and interaction in Work: https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt
- Work versus Codex capabilities: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- ChatGPT Sites supports private preview/refinement before publishing, if available: https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites
- Codex Cloud accessibility varies by plan, environment, and supported workflow: https://help.openai.com/en/articles/20001545-using-codex-cloud

**Boundary:** development-tools research only. NOVA Cloud Engine production, AGOURA indicator, trading and personal accounts untouched.
