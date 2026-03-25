---
name: opencode-pty
description: "Interactive PTY (pseudo-terminal) management for OpenCode. Use when Claude needs to run: (1) Long-running processes (dev servers, npm run dev, cargo watch, database servers, tunnels), (2) Watch modes (npm test -- --watch), (3) Interactive programs (Python REPL, Node REPL, prompts), (4) Background processes that require sending input or reading output on demand. Provides tools: pty_spawn, pty_write, pty_read, pty_list, pty_kill. NOT for simple one-off commands - use bash tool for those."
---

# OpenCode PTY Plugin

## Overview

This skill enables Claude to run interactive terminal sessions with full control over background processes, enabling workflows that the built-in bash tool cannot handle.

## When to Use PTY Tools

Use PTY tools instead of bash when:

- Running dev servers (`npm run dev`, `cargo watch`, `python manage.py runserver`)
- Running watch modes (`npm test -- --watch`, `cargo build --watch`)
- Running long-running processes (database servers, tunnels, proxies)
- Interactive programs (REPLs, prompts, CLIs with menus)
- Any process that doesn't terminate automatically

## Tool Reference

### pty_spawn

Start a new PTY session for a long-running process.

```json
{
  "command": "npm",
  "args": ["run", "dev"],
  "workdir": "/path/to/project",
  "title": "Dev Server",
  "notifyOnExit": true
}
```

Key parameters:
- `command`: The command to run
- `args`: Command arguments as array
- `workdir`: Working directory
- `title`: Human-readable name for the session
- `notifyOnExit`: Get notified when process exits

### pty_write

Send input to a running PTY session. Use for:
- Responding to prompts
- Typing commands in REPL
- Sending keyboard shortcuts (Ctrl+C = `\x03`, Ctrl+D = `\x04`)

```json
{
  "id": "pty_XXXXXXXX",
  "data": "hello world\n"
}
```

Common escape sequences:
- `\x03` = Ctrl+C (interrupt)
- `\x04` = Ctrl+D (EOF)
- `\x1a` = Ctrl+Z (suspend)
- `\t` = Tab
- `\n` = Enter

### pty_read

Read output from a PTY session with optional regex filtering.

```json
{
  "id": "pty_XXXXXXXX",
  "pattern": "error|ERROR",
  "limit": 50
}
```

- Use `pattern` to filter lines matching regex
- Use `limit` to control output pagination
- Returns line numbers for easy navigation

### pty_list

List all active PTY sessions with status, PID, and line count.

### pty_kill

Terminate a PTY session.

```json
{
  "id": "pty_XXXXXXXX",
  "cleanup": true
}
```

Use `cleanup: true` to remove the session from the list.

## Common Workflows

### Running a Dev Server

1. Spawn the dev server with `pty_spawn`
2. Read output with `pty_read` to check for ready status
3. Continue with development tasks
4. Kill with `pty_kill` when done

### Interactive REPL Session

1. Spawn the REPL (`python`, `node`, `irb`)
2. Write commands with `pty_write`
3. Read results with `pty_read`
4. Send Ctrl+C to interrupt if needed
5. Kill when done

### Watch Mode

1. Spawn the watch command
2. Read output to see build/test results
3. Make code changes
4. Read output again to see results
5. Kill when done

## Example Session

```bash
# Start dev server
pty_spawn: command="npm", args=["run", "dev"], workdir="/project", title="Dev Server"

# Wait and check output
pty_read: id="pty_123456", limit=30

# Server is ready, continue working...
# Later, kill the server
pty_kill: id="pty_123456"
```