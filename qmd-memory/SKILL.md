---
name: qmd-memory
description: Configure and troubleshoot OpenClaw memory with the experimental QMD backend. Use when enabling `memory.backend = "qmd"`, installing QMD prerequisites (Bun, SQLite extension support), indexing workspace memory files, running initial `qmd update/embed`, or validating recall with test queries.
---

# QMD Memory for OpenClaw

## Verify prerequisites

Run:

```bash
brew update
brew install oven-sh/bun/bun sqlite
bun install -g @tobilu/qmd
```

If Bun blocks lifecycle scripts, run:

```bash
bun pm -g trust @tobilu/qmd node-llama-cpp
```

## Use a stable qmd command for gateway

Prefer a wrapper script with absolute paths so launchd/gateway PATH differences do not break QMD:

```bash
mkdir -p ~/.openclaw/bin
cat > ~/.openclaw/bin/qmd-openclaw <<'EOF'
#!/bin/sh
exec /opt/homebrew/bin/node /Users/autobot/.bun/install/global/node_modules/@tobilu/qmd/dist/cli/qmd.js "$@"
EOF
chmod +x ~/.openclaw/bin/qmd-openclaw
```

## Configure OpenClaw

Set in `openclaw.json`:

- `memory.backend = "qmd"`
- `memory.qmd.command = "~/.openclaw/bin/qmd-openclaw"`
- `memory.qmd.includeDefaultMemory = true`
- Add memory paths in `memory.qmd.paths`:
  - workspace root pattern: `MEMORY.md`
  - workspace memory dir pattern: `**/*.md`

## Build and warm the index

Use the same XDG dirs OpenClaw uses:

```bash
STATE_DIR="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
export XDG_CONFIG_HOME="$STATE_DIR/agents/main/qmd/xdg-config"
export XDG_CACHE_HOME="$STATE_DIR/agents/main/qmd/xdg-cache"

qmd collection list
qmd update
qmd embed
qmd search "memory test" --json
```

## Quick troubleshooting

- `sqlite-vec is not available`: run QMD with Node wrapper (above), not Bun runtime.
- `qmd not found`: set `memory.qmd.command` to an absolute path.
- Empty results: confirm collections include `MEMORY.md` and `memory/*.md`, then re-run `qmd update && qmd embed`.
