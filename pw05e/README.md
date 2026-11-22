# PW-05E — Combined Linux sandbox compatibility and editable browser preview

**Status: prepared, Work execution not yet performed.** Scope: development-tooling research only, no production changes.

## Verified checkpoints

- PW-03: standalone isolated Playwright MCP browser client passed, not authenticated Codex-to-MCP.
- PW-04: six auth classifier tests passed; GitHub Actions Codex had no auth.
- PW-05: Work Codex authentication reported; Docker socket denied.
- PW-05B/PW-05C: four classification tests passed, but actual `unshare --user --map-root-user --net` failed with `cannot open /proc/self/uid_map: Read-only file system`. This proves that *this namespace creation path* failed, not that every host-supported sandbox backend is impossible.
- PW-05C Plan B: Work Cloud Browser passed navigation, inspection, text input, checkbox and deletion on public React TodoMVC; local loopback preview socket failed `PermissionError: [Errno 1] Operation not permitted`; source-edit/retest still unproven.
- PW-05D: private preview bridge options documented, not tested. Read `pw05d/README.md`.

## One Work batch, two independent lanes

**Lane A: Read-only Linux isolation compatibility audit**

1. Inspect the existing `codex sandbox --help`, `codex --help` and installed sandbox capabilities. Read-only inspect OS/kernel namespace policy and procfs mount metadata only when supported and authorized. No `unshare` retries necessary.
2. Determine whether the failed `uid_map` write is caused by procfs restrictions or denied user namespace mapping. Do not assert a root cause that inspection cannot prove.
3. Evaluate whether an existing, *already-authorized* sandbox backend can restrict the MCP process **and** spawned Chromium process, including filesystem, secrets, network egress and process access. Do not infer that a sandboxed Codex process automatically sandboxes MCP children.
4. Document exact allowed configuration route (if any). Do **not** launch MCP, install dependencies, change sysctls, mounts, network policy, Docker privileges or permissions.
5. Classify `SUPPORTED_AND_VERIFIED`, `CONFIGURATION_POSSIBLE_UNVERIFIED` or `HOST_RESTRICTION_BLOCKED`, with specific evidence. Never mark full agent/MCP integration PASS from CLI help.

**Lane B: Editable preview bridge capability audit**

1. In the same Work session, discover whether a native private local HTML preview, browser-openable scratch artifact, existing first-party Sites private preview, or preexisting Codex Cloud preview is actually supported. Do not create a Site or deployment without approval.
2. If a fully ephemeral scratch preview is supported, use only `pw05c/fixture.html` in a disposable copy. Observe wrong status `Items: 2` after one item, repair the source in scratch, reload and verify `Items: 1` and Reset `Items: 0`.
3. If the bridge is not supported, report exact blocker. Do not expose a public port, create credentials, publish a site, install packages or weaken security. Do not rerun the already-passed TodoMVC test.
4. Distinguish a simple HTML preview from a private multi-file repository development preview. Passing the former is not evidence of the latter.

## Report once, at end of batch

| Requirement | Plan A: Codex + Playwright MCP | Plan B: Work Cloud Browser |
|---|---|---|
| Available and authorized isolation | | |
| Direct browser control | | |
| Access to editable scratch source | | |
| Code edit and browser reload | | |
| Retest observable UI state | | |
| Same agent/session, no manual actions | | |
| Applicability to private NOVA development repo | | |
| Remaining blocker and safest next step | | |

Keep evidence labeled as **observed**, **documented**, or **unproven**. Stop unsafe tests and continue safe checks on the other lane. No new paid model calls, credentials, GitHub writes, deployment, or production changes.

**End condition:** either a demonstrated full disposable edit/retest loop, or an accurate bounded explanation of what runtime capability or authorization is missing. Do not claim completion of Playwright MCP integration without a trace of an actual agent-to-MCP browser tool invocation.
