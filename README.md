# OpenCode Windows Desktop Setup

Complete MCP and Skills configuration for OpenCode Desktop on Windows, migrated from WSL Ubuntu setup.

## Overview

This repository documents the complete setup of MCPs (Model Context Protocols) and Skills for OpenCode Desktop on Windows, including:

- 4 MCP servers (chrome-devtools, context7, deepwiki, tavily)
- 32 Skills for various development workflows
- Chrome DevTools integration with dedicated CDP profile
- DeepWiki bridge for documentation access

## Installation

### Prerequisites

1. OpenCode Desktop installed on Windows
2. Node.js and npm installed
3. Python 3 installed
4. Chrome browser installed

### Quick Setup

1. **Install Python requests (for DeepWiki bridge):**
   ```powershell
   pip install requests
   ```

2. **Create config directory:**
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.config\opencode"
   ```

3. **Copy the configuration file:**
   ```powershell
   Copy-Item opencode.jsonc "$env:USERPROFILE\.config\opencode\opencode.jsonc" -Force
   ```

4. **Copy skills:**
   ```powershell
   Copy-Item -Recurse skills "$env:USERPROFILE\.config\opencode\" -Force
   ```

5. **Copy DeepWiki bridge:**
   ```powershell
   Copy-Item -Recurse deepwiki-bridge "$env:USERPROFILE\.config\opencode\" -Force
   ```

6. **Create Chrome CDP profile directory:**
   ```powershell
   New-Item -ItemType Directory -Force -Path "$env:LOCALAPPDATA\ChromeCDPProfile"
   ```

7. **Restart OpenCode Desktop** to load the new configuration

## Configuration

### File Structure

```
%USERPROFILE%\.config\opencode/
├── opencode.jsonc          # Main configuration
├── skills/                 # 32 skill directories
│   ├── agent-browser/
│   ├── chrome-devtools-windows/   # Chrome CDP setup skill
│   ├── context7/
│   ├── crawl/
│   ├── database-migration/
│   ├── deepwiki/
│   ├── dispatching-parallel-agents/
│   ├── docker-expert/
│   ├── extract/
│   ├── find-skills/
│   ├── frontend-design/
│   ├── git-advanced-workflows/
│   ├── mermaid-diagrams/
│   ├── next-best-practices/
│   ├── nse-stock-analyzer/
│   ├── opencode-pty/
│   ├── opencontext/
│   ├── pdf/
│   ├── protocol-reverse-engineering/
│   ├── python-performance-optimization/
│   ├── remotion-best-practices/
│   ├── rust-async-patterns/
│   ├── schematics-pdf-analyser/
│   ├── search/
│   ├── skill-creator/
│   ├── supabase-postgres-best-practices/
│   ├── systematic-debugging/
│   ├── tavily-best-practices/
│   ├── ui-ux-pro-max/
│   ├── vercel-react-best-practices/
│   ├── vercel-react-native-skills/
│   ├── vue-best-practices/
│   └── web-design-guidelines/
└── deepwiki-bridge/
    └── bridge.py           # DeepWiki MCP bridge

%LOCALAPPDATA%\ChromeCDPProfile/   # Dedicated Chrome CDP profile
```

## MCPs

### chrome-devtools

**Purpose:** Browser automation via Chrome DevTools Protocol

**Uses a dedicated Chrome profile** at `C:\Users\%USERNAME%\AppData\Local\ChromeCDPProfile` - separate from your main Chrome.

**Installation:** Uses `npx chrome-devtools-mcp@latest` - no global installation required. Downloaded automatically on first use.

**Setup:**
1. Launch Chrome with remote debugging:
   ```powershell
   Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "--remote-debugging-port=9333","--remote-debugging-address=127.0.0.1","--user-data-dir=$env:LOCALAPPDATA\ChromeCDPProfile","--no-first-run","--no-default-browser-check","about:blank"
   ```

2. **First time only:** Sign in with your Google account. Sessions persist for future launches.

3. Verify Chrome is listening:
   ```powershell
   Invoke-WebRequest -Uri "http://127.0.0.1:9333/json/version" -UseBasicParsing
   ```

**Timeout:** 300000ms (5 minutes)

**Note:** The MCP will fail with error -32000 if Chrome is not running with CDP enabled. Always start Chrome first before using the MCP.

### context7

**Purpose:** Code context search via Context7 API

**Environment:**
- `CONTEXT7_API_KEY`: Your Context7 API key

**Timeout:** 150000ms (2.5 minutes)

**Note:** Installed via npx, no additional setup required

### deepwiki

**Purpose:** Access DeepWiki documentation

**Bridge Location:** `C:\Users\%USERNAME%\.config\opencode\deepwiki-bridge\bridge.py`

**Requirements:**
- Python 3
- requests library (`pip install requests`)

**Timeout:** 150000ms (2.5 minutes)

### tavily

**Purpose:** Web search via Tavily API

**Environment:**
- `TAVILY_API_KEY`: Your Tavily API key

**Timeout:** 150000ms (2.5 minutes)

**Note:** Installed via npx, no additional setup required

## MCP Timeout Reference

| MCP | Timeout | Reason |
|-----|---------|--------|
| chrome-devtools | 300000ms (5 min) | Browser operations can be slow |
| context7 | 150000ms (2.5 min) | API + npx download time |
| deepwiki | 150000ms (2.5 min) | Network requests |
| tavily | 150000ms (2.5 min) | API + npx download time |

**Default timeout is 5000ms** if not specified - too short for npx downloads!

## Skills Reference

### Development & Code

| Skill | Description |
|-------|-------------|
| `agent-browser` | Browser automation and web testing |
| `context7` | Code context search |
| `crawl` | Website crawling |
| `extract` | Content extraction from URLs |
| `next-best-practices` | Next.js best practices |
| `vercel-react-best-practices` | React optimization guidelines |
| `vercel-react-native-skills` | React Native best practices |
| `vue-best-practices` | Vue.js best practices |

### DevOps & Infrastructure

| Skill | Description |
|-------|-------------|
| `docker-expert` | Docker containerization |
| `database-migration` | Database migrations |
| `supabase-postgres-best-practices` | PostgreSQL optimization |
| `git-advanced-workflows` | Advanced Git workflows |

### AI/ML & Data

| Skill | Description |
|-------|-------------|
| `python-performance-optimization` | Python profiling and optimization |
| `rust-async-patterns` | Rust async programming |
| `nse-stock-analyzer` | NSE stock analysis |
| `protocol-reverse-engineering` | Network protocol analysis |

### Utilities

| Skill | Description |
|-------|-------------|
| `chrome-devtools-windows` | Chrome CDP setup for Windows |
| `opencode-pty` | PTY management for long-running processes |
| `opencontext` | Git-style context management for AI sessions |
| `pdf` | PDF manipulation |
| `search` | Web search |
| `mermaid-diagrams` | Diagram creation |
| `schematics-pdf-analyser` | Electronics repair instructor |
| `ui-ux-pro-max` | UI/UX design |
| `web-design-guidelines` | Web design best practices |

### Meta

| Skill | Description |
|-------|-------------|
| `skill-creator` | Create custom skills |
| `find-skills` | Discover available skills |
| `dispatching-parallel-agents` | Parallel agent dispatch |
| `systematic-debugging` | Debugging methodology |
| `tavily-best-practices` | Tavily integration best practices |
| `frontend-design` | Frontend design patterns |
| `remotion-best-practices` | Remotion video creation |

## Providers

The configuration includes 4 AI providers:

1. **Chutes AI** - Various models (Kimi K2, GLM, MiniMax)
2. **Alibaba DashScope** - Chinese models (Qwen, GLM)
3. **Google** - Gemini and Claude models via Antigravity
4. **Ollama** - Local models

## Troubleshooting

### MCP Timeout Issues

If MCPs show "Request timed out" errors:

1. **Check timeout values** in `opencode.jsonc` - should be 150000+ for npx-based MCPs
2. **Check network connectivity** for API-based MCPs (context7, tavily)
3. **First run takes longer** - npx needs to download packages

### Chrome DevTools Error 32000

Error 32000 = Chrome is not running with CDP enabled.

1. **Kill all Chrome processes:**
   ```powershell
   Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
   ```

2. **Launch Chrome with CDP flags:**
   ```powershell
   Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "--remote-debugging-port=9333","--remote-debugging-address=127.0.0.1","--user-data-dir=$env:LOCALAPPDATA\ChromeCDPProfile","--no-first-run","--no-default-browser-check","about:blank"
   ```

3. **Wait 3-4 seconds**, then verify:
   ```powershell
   Invoke-WebRequest -Uri "http://127.0.0.1:9333/json/version" -UseBasicParsing
   ```

4. **Restart the MCP** in OpenCode Desktop (toggle off/on)

### Chrome DevTools Connection Failed

1. Ensure Chrome is launched with remote debugging
2. Check that the CDP profile directory exists
3. Verify port 9333 is not in use by another process:
   ```powershell
   netstat -ano | Select-String ":9333"
   ```

### Skills Not Loading

1. Verify skills are in the correct directory:
   ```powershell
   ls "$env:USERPROFILE\.config\opencode\skills"
   ```

2. Check that each skill has a `SKILL.md` file

3. Restart OpenCode Desktop

### npx Package Download Slow

First run of `npx -y @upstash/context7-mcp` or `npx -y tavily-mcp@latest` downloads the package. This can take 30-60 seconds on slow connections.

**Solution:** Increase timeout to 150000ms (already done in config)

## Migration from WSL

This setup was migrated from WSL Ubuntu to Windows. Key changes:

- **Paths**: WSL paths (`/home/vic/...`) → Windows paths (`C:\Users\...`)
- **Chrome Profile**: Dedicated CDP profile instead of WSL Chrome
- **Node**: WSL node → Windows node
- **Python**: WSL python3 → Windows python
- **Timeouts**: Increased from default 5000ms to 150000ms+

## Contributing

Feel free to submit issues or PRs if you find bugs or want to add more skills.

## License

MIT