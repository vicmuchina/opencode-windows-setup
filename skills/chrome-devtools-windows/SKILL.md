---
name: chrome-devtools-windows
description: Chrome DevTools Protocol integration for Windows - launch Chrome with remote debugging and verify connection for browser automation.
---

# Chrome DevTools MCP Setup (Windows)

## Overview

This skill provides the complete workflow to launch Google Chrome on Windows with remote debugging enabled, allowing the chrome-devtools MCP to control the browser for automation tasks.

## When to Use

Use this skill when:
- The chrome-devtools MCP shows "failed" or "connection closed" status
- You need to start browser automation tasks
- Chrome needs to be launched with CDP (Chrome DevTools Protocol) enabled
- Setting up fresh Chrome DevTools integration

## Quick Start

### Step 1: Launch Chrome with Remote Debugging

Run this PowerShell command to launch Chrome with CDP enabled on port 9333:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --remote-debugging-port=9333 `
  --remote-debugging-address=127.0.0.1 `
  --user-data-dir="C:\Users\steph\AppData\Local\Google\Chrome\User Data" `
  --profile-directory=Default `
  --no-first-run `
  --no-default-browser-check
```

**One-liner version:**
```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9333 --remote-debugging-address=127.0.0.1 --user-data-dir="C:\Users\steph\AppData\Local\Google\Chrome\User Data" --profile-directory=Default --no-first-run --no-default-browser-check
```

### Step 2: Verify Chrome is Listening

After Chrome launches, verify the CDP endpoint is accessible:

```powershell
curl http://127.0.0.1:9333/json/version
```

**Expected output:**
```json
{
  "Browser": "Chrome/146.0.7680.164",
  "Protocol-Version": "1.3",
  "User-Agent": "...",
  "V8-Version": "...",
  "WebKit-Version": "..."
}
```

If you see JSON output, Chrome is ready for the MCP to connect.

### Step 3: Check MCP Status

In OpenCode Desktop, check the MCPs panel. The chrome-devtools MCP should now show "connected" instead of "failed".

## Chrome Profile

**Profile Location:** `C:\Users\steph\AppData\Local\Google\Chrome\User Data\Default`

This uses your existing Chrome profile, so:
- ✅ Bookmarks are preserved
- ✅ Extensions are available
- ✅ Login sessions persist
- ✅ History is maintained

## Troubleshooting

### Chrome Already Running Without CDP

If Chrome is already running without remote debugging:

1. **Close all Chrome windows completely**
2. **Check for background processes:**
   ```powershell
   taskkill /F /IM chrome.exe
   ```
3. **Relaunch with CDP flags** (use the command above)

### Port 9333 Already in Use

If port 9333 is occupied:

1. **Find what's using the port:**
   ```powershell
   netstat -ano | findstr :9333
   ```

2. **Kill the process or use a different port** (e.g., 9334):
   ```powershell
   & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9334 --remote-debugging-address=127.0.0.1 --user-data-dir="C:\Users\steph\AppData\Local\Google\Chrome\User Data" --profile-directory=Default
   ```

3. **Update the MCP config** if using a different port

### Connection Refused

If `curl http://127.0.0.1:9333/json/version` returns "connection refused":

1. **Verify Chrome is running:**
   ```powershell
   Get-Process chrome
   ```

2. **Check Chrome was launched with correct flags:**
   - Look for `--remote-debugging-port=9333` in the command line

3. **Try localhost instead:**
   ```powershell
   curl http://localhost:9333/json/version
   ```

### MCP Still Shows "Failed"

If the MCP still fails after Chrome is running with CDP:

1. **Restart the MCP** in OpenCode Desktop (toggle off/on)
2. **Restart OpenCode Desktop** completely
3. **Check timeout settings** in config (should be 45000ms)
4. **Verify node can reach the endpoint:**
   ```powershell
   node -e "fetch('http://127.0.0.1:9333/json/version').then(r => r.json()).then(console.log)"
   ```

## Chrome Location

**Default Windows Chrome path:**
```
C:\Program Files\Google\Chrome\Application\chrome.exe
```

**Alternative paths:**
- 32-bit: `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- User install: `C:\Users\<username>\AppData\Local\Google\Chrome\Application\chrome.exe`

**Find Chrome path:**
```powershell
(Get-Command chrome).Source
```

## Command Line Flags Explained

| Flag | Purpose |
|------|---------|
| `--remote-debugging-port=9333` | Enable CDP on port 9333 |
| `--remote-debugging-address=127.0.0.1` | Bind to localhost only |
| `--user-data-dir=...` | Use specific profile directory |
| `--profile-directory=Default` | Use the Default profile |
| `--no-first-run` | Skip first-run experience |
| `--no-default-browser-check` | Skip default browser check |

## Automation Workflow

For AI agents automating browser tasks:

1. **Check if Chrome is already running with CDP:**
   ```powershell
   curl -s http://127.0.0.1:9333/json/version
   ```

2. **If fails, launch Chrome with CDP** (use the command above)

3. **Wait 2-3 seconds** for Chrome to fully initialize

4. **Verify connection** with curl command

5. **Proceed with browser automation** via chrome-devtools MCP

## Related MCPs

- **chrome-devtools** - The MCP that uses this CDP connection
- **agent-browser** - Higher-level browser automation skill

## See Also

- Chrome DevTools Protocol documentation: https://chromedevtools.github.io/devtools-protocol/
- chrome-devtools-mcp package: https://github.com/microsoft/chrome-devtools-mcp
