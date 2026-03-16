---
name: openclaw-gateway-watchdog
description: Keep the OpenClaw dashboard/gateway online on macOS by repairing LaunchAgent config, installing a watchdog LaunchAgent, auto-restarting on failed probes, and validating recovery. Use when users report the dashboard going offline and not auto-recovering.
---

# OpenClaw Gateway Watchdog (macOS)

## What this does

- Reinstalls a clean OpenClaw gateway LaunchAgent
- Adds a watchdog script that probes gateway health
- Restarts gateway automatically if probe fails
- Runs every 120 seconds via launchd

## 1) Repair gateway LaunchAgent

```bash
openclaw gateway install --force
openclaw gateway restart
openclaw gateway status
```

## 2) Install watchdog script

Create `~/.openclaw/bin/openclaw-watchdog.sh`:

```bash
#!/bin/zsh
set -u

OPENCLAW_BIN="/opt/homebrew/bin/openclaw"
LOG_FILE="$HOME/.openclaw/logs/watchdog.log"
LOCK_DIR="$HOME/.openclaw/run/watchdog.lock"
TS="$(date '+%Y-%m-%d %H:%M:%S %Z')"

mkdir -p "$HOME/.openclaw/logs" "$HOME/.openclaw/run"

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  exit 0
fi
trap 'rmdir "$LOCK_DIR" >/dev/null 2>&1' EXIT

if "$OPENCLAW_BIN" gateway probe >/dev/null 2>&1; then
  exit 0
fi

echo "[$TS] gateway probe failed; restarting" >> "$LOG_FILE"
"$OPENCLAW_BIN" gateway restart >> "$LOG_FILE" 2>&1 || true
sleep 3

if "$OPENCLAW_BIN" gateway probe >/dev/null 2>&1; then
  echo "[$TS] gateway recovery succeeded" >> "$LOG_FILE"
else
  echo "[$TS] gateway recovery failed" >> "$LOG_FILE"
fi
```

Then:

```bash
chmod +x ~/.openclaw/bin/openclaw-watchdog.sh
```

## 3) Install watchdog LaunchAgent

Create `~/Library/LaunchAgents/ai.openclaw.watchdog.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>ai.openclaw.watchdog</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/zsh</string>
    <string>/Users/autobot/.openclaw/bin/openclaw-watchdog.sh</string>
  </array>
  <key>StartInterval</key><integer>120</integer>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>/Users/autobot/.openclaw/logs/watchdog.launchd.log</string>
  <key>StandardErrorPath</key><string>/Users/autobot/.openclaw/logs/watchdog.launchd.err.log</string>
</dict>
</plist>
```

Load it:

```bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/ai.openclaw.watchdog.plist >/dev/null 2>&1 || true
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.openclaw.watchdog.plist
launchctl enable gui/$(id -u)/ai.openclaw.watchdog
launchctl kickstart -k gui/$(id -u)/ai.openclaw.watchdog
```

## 4) Verify

```bash
openclaw gateway status
launchctl print gui/$(id -u)/ai.openclaw.watchdog | sed -n '1,80p'
tail -f ~/.openclaw/logs/watchdog.log
```

## Optional hardening

Pin trusted plugins to remove auto-load risk:

- Set `plugins.allow` to explicit plugin IDs you trust.
