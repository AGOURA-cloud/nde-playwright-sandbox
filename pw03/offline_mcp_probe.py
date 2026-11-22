"""Offline-only, credential-free MCP protocol and browser proof on an ephemeral CI runner."""
import base64
import json
import queue
import subprocess
import threading
import time
import urllib.parse

IMAGE = "mcr.microsoft.com/playwright/mcp@sha256:77dccc5ce9e94cb8ae7ebea87ddbb6cd54b05760c4d63c54e16accf2726b8734"
NAME = "pw03-synthetic-once"

def docker(*args):
    return subprocess.check_output(["docker", *args], text=True, timeout=40).strip()

def check(msg, okay):
    if not okay:
        raise AssertionError(msg)
    print("PASS " + msg, flush=True)

proc = None
created = False
outq = queue.Queue()
stderr_lines = []

def stdout_reader():
    for line in proc.stdout:
        outq.put(line)
    outq.put(None)

def stderr_reader():
    for line in proc.stderr:
        if len(stderr_lines) < 60:
            stderr_lines.append(line.rstrip())

counter = 0
def send(payload):
    proc.stdin.write(json.dumps({"jsonrpc": "2.0", **payload}) + "\n")
    proc.stdin.flush()

def request(method, params=None):
    global counter
    counter += 1
    rid = counter
    send({"id": rid, "method": method, "params": params or {}})
    deadline = time.monotonic() + 50
    while time.monotonic() < deadline:
        try:
            line = outq.get(timeout=min(10, max(0.1, deadline-time.monotonic())))
        except queue.Empty:
            continue
        if line is None:
            raise RuntimeError("MCP server closed stdout: " + repr(stderr_lines[-10:]))
        resp = json.loads(line)
        if resp.get("id") == rid:
            return resp
        if "id" in resp and "method" in resp:
            send({"id": resp["id"], "error": {"code": -32601, "message": "Unsupported optional client request"}})
    raise TimeoutError("No response to " + method + ": " + repr(stderr_lines[-10:]))

def result(method, params=None):
    resp = request(method, params)
    if "error" in resp:
        raise RuntimeError(method + ": " + str(resp["error"]))
    return resp["result"]

def call(name, args=None):
    response = result("tools/call", {"name": name, "arguments": args or {}})
    if response.get("isError"):
        raise RuntimeError(name + ": " + str(response.get("content"))[:400])
    return response

def text(response):
    return "\n".join(x.get("text", "") for x in response.get("content", []) if x.get("type") == "text")

try:
    docker("create", "-i", "--name", NAME, "--network", "none", "--cap-drop", "ALL",
           "--security-opt", "no-new-privileges", "--user", "node",
           "--pids-limit", "256", "--memory", "2g", "--shm-size", "256m",
           IMAGE, "--isolated", "--output-dir", "/tmp/pw-output")
    created = True
    spec = json.loads(docker("inspect", NAME))[0]
    host = spec["HostConfig"]
    check("network-isolated Docker container", host["NetworkMode"] == "none")
    check("no host mounts, port forwarding or privileged mode",
          not spec["Mounts"] and not host.get("Binds") and not host.get("PortBindings") and not host["Privileged"])
    check("nonroot with dropped capabilities",
          spec["Config"]["User"] == "node" and "ALL" in host["CapDrop"])
    proc = subprocess.Popen(["docker", "start", "-ai", NAME],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True, bufsize=1)
    threading.Thread(target=stdout_reader, daemon=True).start()
    threading.Thread(target=stderr_reader, daemon=True).start()
    init = result("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                  "clientInfo": {"name": "pw03-offline-preflight", "version": "1"}})
    check("MCP initialization", bool(init.get("serverInfo")) and "tools" in init.get("capabilities", {}))
    send({"method": "notifications/initialized"})
    tools = {x["name"] for x in result("tools/list")["tools"]}
    required = {"browser_navigate", "browser_snapshot", "browser_click", "browser_evaluate", "browser_close"}
    check("MCP browser tools listed", required.issubset(tools))
    html = '<!doctype html><title>PW03 fixture</title><h1>PW03 synthetic page</h1><button id="advance" onclick="document.querySelector(\'#state\').textContent=\'complete\'">Advance</button><p id="state">ready</p>'
    call("browser_navigate", {"url": "data:text/html," + urllib.parse.quote(html)})
    check("synthetic page opened", "PW03 synthetic page" in text(call("browser_snapshot")))
    call("browser_click", {"target": "#advance", "element": "Advance button"})
    snapshot = text(call("browser_snapshot"))
    check("synthetic click changed state", "complete" in snapshot and "ready" not in snapshot)
    evaluated = text(call("browser_evaluate", {"function": "() => document.querySelector('#state').textContent"}))
    check("synthetic DOM evaluation", "complete" in evaluated)
    call("browser_close")
    print("PW03_OFFLINE_MCP_PASS", flush=True)
finally:
    if proc is not None:
        try:
            proc.stdin.close()
            proc.wait(timeout=10)
        except (OSError, subprocess.TimeoutExpired):
            proc.kill()
            proc.wait(timeout=10)
    if created:
        docker("rm", "-f", "-v", NAME)
        check("container removed", not docker("ps", "-a", "--filter", "name=^/" + NAME + "$", "--format", "{{.Names}}"))
