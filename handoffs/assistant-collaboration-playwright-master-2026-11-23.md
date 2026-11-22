# Assistant Collaboration + Playwright — Master Handoff and Backlog
Checkpoint date: 2026-11-23
Status: documentation checkpoint; no runtime execution or production modifications.

## Mission
Develop a secure AI-assisted software engineering workflow that can inspect, edit, preview, debug and retest applications with minimal Android-side manual work. Support NOVA Cloud Engine v0.7 and AGOURA V3.0 as **separate** projects. Playwright is development tooling, never market-signal intelligence.

## Scope and boundaries
- NOVA: no production deployment, live trading, credentials, trading-rule changes, or unattended scanning without explicit approval.
- AGOURA: personal TradingView Pine Script indicator; V2.2 Phase E Rejection Audit is frozen; V3.0 implementation not started; research and paper-only.
- Assistant Collaboration Pilot: shared developer tooling only, with distinct repositories, credentials, approval boundaries and evidence.
- Never circumvent host sandbox restrictions, weaken security, expose a preview publicly, install packages, or incur costs without approval.

## Original collaboration pilot — historical report (reverify before acting)
- Repository: `assistant-collab-pilot`.
- Codex-first pilot: 14/14 tests reportedly passed.
- Draft PR #1 reportedly open/unmerged.
- Codex Cloud environment reportedly created.
- Claude independent review planned, not completed.
These are *historical reported states*, not newly checked in this checkpoint.

## Playwright research and evidence
| Phase | Observed or reported result | Remaining limitation |
| --- | --- | --- |
| PW-03 | Standalone MCP client interacted with synthetic offline browser; `PW03_OFFLINE_MCP_PASS`; Codex recognized inert MCP configuration | No authenticated Codex-to-MCP call |
| PW-04 | Six authentication classifier tests passed in Actions | Codex in Actions had `NO_AUTH`; agent not attempted |
| PW-05 | Work Codex CLI authenticated | Docker socket permission denied |
| PW-05B | Four fail-closed classification unit tests passed | Actual namespace creation not demonstrated |
| PW-05C Plan A | `unshare` failed: `cannot open /proc/self/uid_map: Read-only file system` | Direct Playwright MCP blocked/unproven |
| PW-05C Plan B | Work Cloud Browser autonomously navigated/edited public TodoMVC UI | Local loopback scratch preview bind denied; source-edit/retest unproven |
| PW-05D | Private preview bridge research instructions created | Runtime result not yet supplied |
| PW-05E | Dual-track instructions created and verified on GitHub | Work execution pending |

Primary PW-05E checkpoint: https://github.com/AGOURA-cloud/nde-playwright-sandbox/blob/research/pw05e-dual-track-runtime-gates/pw05e/README.md

## Active plans
**A — Authenticated Codex + Playwright MCP:** Read-only investigate supported, authorized Linux isolation backends and secure MCP/Chromium child-process confinement. CLI help alone is not evidence of integration. Do not retry blocked namespace creation or bypass restrictions.

**B — Work Cloud Browser + editable private preview:** Discover supported ephemeral/private preview capabilities without local socket or public deployment. If available, use disposable `pw05c/fixture.html`: Add shows erroneous `Items: 2`; edit scratch source to correct +1; reload and confirm `Items: 1`; Reset confirms `Items: 0`. Distinguish static scratch demo from multi-file private-repo development.

## Prioritized backlog
| Priority | Item | State |
| --- | --- | --- |
| P0 | Preserve verified checkpoints and negative evidence | Ongoing |
| P0 | Run PW-05E Lane A supported-isolation audit | Pending |
| P0 | Run PW-05E Lane B editable-preview audit | Pending |
| P0 | Demonstrate source edit → browser reload → retest in same agent session | Unproven |
| P1 | Prove authenticated Codex agent invokes Playwright MCP browser tool | Unproven |
| P1 | Verify confinement of MCP and browser children, network and secrets | Open |
| P1 | Verify preview access for editable private multi-file repository | Open |
| P1 | Recheck original collaboration pilot repo/PR/cloud environment | Pending |
| P1 | Design independent Codex–Claude review handoff with evidence | Planned |
| P2 | Standardize regression tests, logs and review checkpoints | Planned |
| P2 | Pilot tooling separately on approved NOVA development branch | Future approval |
| P2 | Pilot tooling separately on approved AGOURA development branch | Future approval |
| P3 | Optional repeatable maintenance workflow | Future approval |

## Next approved research
Review PW-05E Work findings once returned. Record each capability as **observed**, **documented but untested**, or **blocked**. Report whether actual agent-to-MCP tool invocation happened, whether scratch code was edited and browser retested, exact host/runtime limitations, and the safest next experiment. Do not claim full integration without end-to-end evidence.

## Reporting format
Completed; evidence and links; failures/uncertainties; changes to backlog; protected-project changes (expected none); recommended next controlled batch.

## Discussion ownership
This normal chat: collaboration architecture, Codex/Claude, Playwright MCP, Work Cloud Browser, safe tooling.
NOVA normal chat: NOVA product architecture and decisions.
AGOURA normal chat: indicator design and decisions.
Private Indicator Work: authorized TradingView execution and tests.

**Checkpoint intent:** A durable recovery document, not an instruction to deploy or start trading.
