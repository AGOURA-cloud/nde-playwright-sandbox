"""PW-05B unprivileged, non-networking capability preflight.

Only requests a new empty network namespace. Does NOT run a browser/MCP,
open sockets, inspect credentials, install packages or alter system settings.
"""
import json
import os
import shutil
import subprocess


def classify_namespace(returncode, host_ns, child_ns):
    """Never promote a namespace probe to full security validation."""
    if returncode != 0 or not host_ns or not child_ns:
        return "BLOCKED_OR_UNVERIFIED"
    if child_ns == host_ns:
        return "NOT_ISOLATED"
    return "NETWORK_NAMESPACE_CREATED_ONLY"


def probe() -> dict:
    out = {
        "check": "PW05B_NON_DESTRUCTIVE_PROBE",
        "tools_present": {x: bool(shutil.which(x)) for x in ("codex", "bwrap", "unshare")},
        "work_runtime_isolation_verified": False,
        "mcp_or_browser_started": False,
    }
    try:
        host_ns = os.readlink("/proc/self/ns/net")
    except OSError:
        host_ns = None
    child_ns = None
    returncode = None
    if shutil.which("unshare"):
        try:
            p = subprocess.run(
                ["unshare", "--user", "--map-root-user", "--net", "--",
                 "readlink", "/proc/self/ns/net"],
                capture_output=True, text=True, timeout=8, check=False,
            )
            returncode = p.returncode
            if p.returncode == 0:
                child_ns = p.stdout.strip()
            else:
                out["unshare_error_class"] = "NAMESPACE_NOT_PERMITTED_OR_UNAVAILABLE"
        except (OSError, subprocess.TimeoutExpired):
            out["unshare_error_class"] = "NAMESPACE_PROBE_FAILED"
    else:
        out["unshare_error_class"] = "UNSHARE_TOOL_MISSING"
    out["network_namespace_status"] = classify_namespace(returncode, host_ns, child_ns)
    out["next_step"] = (
        "STOP: Work isolation unverified. No browser/MCP permitted."
        if out["network_namespace_status"] != "NETWORK_NAMESPACE_CREATED_ONLY"
        else "PROVISIONAL ONLY: requires independent full filesystem, egress and MCP-process isolation verification. No browser/MCP permitted yet."
    )
    return out


if __name__ == "__main__":
    print(json.dumps(probe(), sort_keys=True, indent=2))
