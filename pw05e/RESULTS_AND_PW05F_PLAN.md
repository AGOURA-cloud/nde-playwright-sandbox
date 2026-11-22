# PW-05E Result Checkpoint and PW-05F Proposed Next Gate
Date: 2026-11-23
Source: user-supplied Work session report. This checkpoint records reported observations; raw Work logs were not independently fetched here.

## PW-05E findings
| Lane | Classification | Reported evidence |
| --- | --- | --- |
| A: namespace | HOST_RESTRICTION_BLOCKED for tested path | Linux 6.18.57; `findmnt` resolved `/proc/self/uid_map` to read-only `/proc`; nonzero namespace limit; seccomp active but no proven causal involvement |
| A: alternative sandbox | CONFIGURATION_POSSIBLE_UNVERIFIED | Codex CLI 0.172.0-alpha.2 stdio MCP command and `codex sandbox --permission-profile <NAME>`; bubblewrap 0.12.0 installed; no verified profile confines MCP and Chromium children across filesystem, secrets, network and processes; no MCP launched |
| B: managed Sites preview | BLOCKED | Disposable fixture copied and blob verified; `sites-preview start` exited 1 with `listen EPERM: operation not permitted 127.0.0.1:4173`; status stopped |
| B: serverless HTML | BLOCKED | Cloud Browser URL policy rejected `data:text/html`; only HTTP(S) allowed |
| B: Codex Cloud / hosted Sites | AVAILABLE BUT UNPROVEN | One SSH portal, no HTTP preview; `codex cloud --help` no preview command; private hosting tooling available, but no creation/deployment authorized |
| B: full browser loop | UNPROVEN | Prior PW-05C direct interaction PASS; editable source prepared but never rendered; neither erroneous `Items: 2` nor repaired `Items: 1`/Reset `Items: 0` observed |

Reported cleanup: scratch directory removed and absence verified. No repeated blocked probes, installs, credentials, paid calls, security changes, deployments, production modifications or trading. User reports successful isolated Actions run; link/run ID not included in the supplied report.

## Implications
- Do not retry user namespace writes or local loopback preview in the same restricted host.
- CLI flags and installed bubblewrap do not prove safe end-to-end sandbox confinement.
- GitHub Actions isolated browser regressions are proven useful, but are not a substitute for the desired same-agent interactive browser development loop.
- No authenticated Codex-to-Playwright MCP tool invocation has been demonstrated.

## PW-05F proposed (NOT executed): authorized private HTTP preview gate
Goal: identify a disposable, provider-managed environment with a functioning **private HTTP(S) preview**, without changing existing Work host restrictions.

1. Discovery-only: check already available authorized preview-capable environments and their access-control/isolation properties. Do not provision, publish, incur costs or install anything without approval.
2. If a pre-existing approved private preview is available, run disposable `pw05c/fixture.html` in it: click Add and observe `Items: 2`; edit scratch source; reload and verify `Items: 1`; Reset and verify `Items: 0`.
3. Record whether the *same* agent navigates, edits, reloads and retests without user steps; confirm preview is private, access controlled and ephemeral.
4. Only after one-file success, test a synthetic multi-file app in an isolated environment; never touch NOVA/AGOURA code at this stage.
5. Keep direct MCP sandbox research separate; only launch with verified authorized confinement for both MCP server and browser children.

### Stop conditions
No authorized private HTTP preview; required deployment or paid provisioning; credentials or new permissions needed; preview is public; any host security bypass. Stop and request explicit approval, providing options and exact implications.

### Reporting
Classify observed vs documented vs unverified, include command outcomes, preview privacy evidence, browser interaction and source-edit/retest evidence, cleanup, costs and next approval gate.
