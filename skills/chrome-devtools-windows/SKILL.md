---
name: chrome-devtools-windows
description: Chrome DevTools Protocol integration for Windows - launch Chrome with remote debugging and verify connection for browser automation.
---

# Chrome DevTools MCP Setup (Windows)

## Overview

This skill provides the complete workflow to launch Google Chrome on Windows with remote debugging enabled, allowing the chrome-devtools MCP to control the browser for automation tasks.

**Uses a dedicated CDP profile** at `C:\Users\steph\AppData\Local\ChromeCDPProfile` - separate from your main Chrome, keeping them independent.

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
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "--remote-debugging-port=9333","--remote-debugging-address=127.0.0.1","--user-data-dir=C:\Users\steph\AppData\Local\ChromeCDPProfile","--no-first-run","--no-default-browser-check","about:blank"
```

### Step 2: Sign In (First Time Only)

**If this is the first time launching the CDP profile:**
1. Chrome will open with a fresh profile
2. Sign in with your Google account
3. Your logins will persist for future sessions

**Subsequent launches:** Your session will be preserved - no need to sign in again.

### Step 3: Verify Chrome is Listening

After Chrome launches, verify the CDP endpoint is accessible:

```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:9333/json/version" -UseBasicParsing | Select-Object -ExpandProperty Content
```

**Expected output:**
```json
{
   "Browser": "Chrome/146.0.7680.165",
   "Protocol-Version": "1.3",
   "webSocketDebuggerUrl": "ws://127.0.0.1:9333/devtools/browser/..."
}
```

If you see JSON output, Chrome is ready for the MCP to connect.

### Step 4: Check MCP Status

In OpenCode Desktop, check the MCPs panel. The chrome-devtools MCP should now show "connected" instead of "failed".

## Chrome Profile

**CDP Profile Location:** `C:\Users\steph\AppData\Local\ChromeCDPProfile`

This is a **dedicated profile for OpenCode**, separate from your main Chrome:
- ✅ Independent from your regular Chrome
- ✅ Sessions persist across launches
- ✅ Sign in once, stays logged in
- ✅ No interference with normal browsing

## Automation Workflow

For AI agents automating browser tasks:

### 1. Check if Chrome CDP is already running
```powershell
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:9333/json/version" -UseBasicParsing -TimeoutSec 3
    Write-Host "CDP already running"
} catch {
    Write-Host "CDP not running, need to launch Chrome"
}
```

### 2. If not running, launch Chrome with CDP
```powershell
# Kill any existing Chrome using the CDP profile
Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 2

# Launch Chrome with CDP
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "--remote-debugging-port=9333","--remote-debugging-address=127.0.0.1","--user-data-dir=C:\Users\steph\AppData\Local\ChromeCDPProfile","--no-first-run","--no-default-browser-check","about:blank"
```

### 3. Wait and verify
```powershell
Start-Sleep -Seconds 3
Invoke-WebRequest -Uri "http://127.0.0.1:9333/json/version" -UseBasicParsing
```

### 4. Proceed with browser automation via chrome-devtools MCP

## Troubleshooting

### Port 9333 Already in Use

If port 9333 is occupied:

1. **Find what's using the port:**
   ```powershell
   netstat -ano | Select-String ":9333"
   ```

2. **Kill Chrome and relaunch:**
   ```powershell
   Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
   Start-Sleep -Seconds 2
   # Then relaunch with the command above
   ```

### Connection Refused

If the CDP endpoint returns "connection refused":

1. **Verify Chrome is running:**
   ```powershell
   Get-Process chrome
   ```

2. **Check Chrome was launched with correct flags** - the CDP Chrome uses a separate profile

3. **Try localhost instead of 127.0.0.1:**
   ```powershell
   Invoke-WebRequest -Uri "http://localhost:9333/json/version" -UseBasicParsing
   ```

### MCP Still Shows "Failed" or Error 32000

Error 32000 = Chrome is not running with CDP enabled.

1. **Ensure Chrome is launched with CDP flags** (use the command above)
2. **Verify CDP is listening** with the curl/Invoke-WebRequest command
3. **Restart the MCP** in OpenCode Desktop (toggle off/on)
4. **Restart OpenCode Desktop** completely

### Chrome Opens but No CDP

If Chrome opens but CDP doesn't work:
- Another Chrome instance might be interfering
- Kill ALL Chrome processes first:
  ```powershell
  Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
  ```
- Wait 2-3 seconds
- Launch Chrome with CDP flags again

## Chrome Location

**Default Windows Chrome path:**
```
C:\Program Files\Google\Chrome\Application\chrome.exe
```

**Alternative paths:**
- 32-bit: `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- User install: `C:\Users\<username>\AppData\Local\Google\Chrome\Application\chrome.exe`

## Command Line Flags Explained

| Flag | Purpose |
|------|---------|
| `--remote-debugging-port=9333` | Enable CDP on port 9333 |
| `--remote-debugging-address=127.0.0.1` | Bind to localhost only |
| `--user-data-dir=...` | Use dedicated CDP profile directory |
| `--no-first-run` | Skip first-run experience |
| `--no-default-browser-check` | Skip default browser check |
| `about:blank` | Start with blank page |

## Related MCPs

- **chrome-devtools** - The MCP that uses this CDP connection
- **agent-browser** - Higher-level browser automation skill

## See Also

- Chrome DevTools Protocol documentation: https://chromedevtools.github.io/devtools-protocol/
- chrome-devtools-mcp package: https://github.com/microsoft/chrome-devtools-mcp