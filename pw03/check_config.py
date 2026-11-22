"""Static fail-closed checks of the PW-03 example. No network or Docker use."""
from pathlib import Path
import tomllib

base = Path(__file__).resolve().parent
raw = (base / "codex-playwright-offline.example.toml").read_bytes()
conf = tomllib.loads(raw.decode("utf-8"))
mcp = conf["mcp_servers"]["playwright_offline"]
assert mcp["enabled"] is False
assert mcp["required"] is False
assert mcp["command"] == "docker"
assert mcp["default_tools_approval_mode"] == "prompt"
args = mcp["args"]
assert args[:4] == ["run", "--rm", "-i", "--init"]
assert args[args.index("--network") + 1] == "none"
assert args[args.index("--cap-drop") + 1] == "ALL"
assert args[args.index("--user") + 1] == "node"
assert "--isolated" in args
assert "--security-opt" in args and "no-new-privileges" in args
assert not set(args).intersection({"--privileged", "--volume", "-v", "--mount", "--publish", "-p", "--env", "-e", "--net", "--network=host"})
images = [x for x in args if x.startswith("mcr.microsoft.com/")]
assert images == ["mcr.microsoft.com/playwright/mcp@sha256:77dccc5ce9e94cb8ae7ebea87ddbb6cd54b05760c4d63c54e16accf2726b8734"]
assert set(mcp["enabled_tools"]) == {"browser_navigate", "browser_snapshot", "browser_click", "browser_evaluate", "browser_take_screenshot", "browser_close"}
assert not any(x in raw.lower() for x in (b"api_key=", b"password=", b"access_token=", b"secret="))
print("PASS PW03 inert offline Codex config: TOML valid, disabled, no network/mounts/credentials, pinned image, approval prompt")
