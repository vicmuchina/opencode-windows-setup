# OpenCode Windows Desktop Setup

Complete MCP and Skills configuration for OpenCode Desktop on Windows, migrated from WSL Ubuntu setup.

## Overview

This repository documents the complete setup of MCPs (Model Context Protocols) and Skills for OpenCode Desktop on Windows, including:

- 4 MCP servers (chrome-devtools, context7, deepwiki, tavily)
- 31 Skills for various development workflows
- Chrome DevTools integration with Windows Chrome profile
- DeepWiki bridge for documentation access

## Installation

### Prerequisites

1. OpenCode Desktop installed on Windows
2. Node.js and npm installed
3. Python 3 installed
4. Chrome browser installed

### Quick Setup

1. **Install chrome-devtools-mcp globally:**
   ```powershell
   npm install -g chrome-devtools-mcp
   ```

2. **Install Python requests (for DeepWiki bridge):**
   ```powershell
   pip install requests
   ```

3. **Create config directory:**
   ```powershell
   mkdir -p "$env:USERPROFILE\.config\opencode"
   ```

4. **Copy the configuration file:**
   ```powershell
   Copy-Item opencode.jsonc "$env:USERPROFILE\.config\opencode\opencode.jsonc"
   ```

5. **Copy skills:**
   ```powershell
   Copy-Item -Recurse skills "$env:USERPROFILE\.config\opencode\"
   ```

6. **Copy DeepWiki bridge:**
   ```powershell
   Copy-Item -Recurse deepwiki-bridge "$env:USERPROFILE\.config\opencode\"
   ```

## Configuration

### File Structure

```
%USERPROFILE%\.config\opencode/
├── opencode.jsonc          # Main configuration
├── skills/                 # 31 skill directories
│   ├── agent-browser/
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
```

## MCPs

### chrome-devtools

**Purpose:** Browser automation via Chrome DevTools Protocol

**Setup:**
1. Launch Chrome with remote debugging:
   ```powershell
   & "C:\Program Files\Google\Chrome\Application\chrome.exe" `
     --remote-debugging-port=9333 `
     --remote-debugging-address=127.0.0.1 `
     --user-data-dir="$env:LOCALAPPDATA\Google\Chrome\User Data" `
     --profile-directory=Default `
     --no-first-run `
     --no-default-browser-check
   ```

2. Verify Chrome is listening:
   ```powershell
   curl http://127.0.0.1:9333/json/version
   ```

**Profile:** Uses your existing Chrome profile at `C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default`


### context7

**Purpose:** Code context search via Context7 API

**Environment:**
- `CONTEXT7_API_KEY`: Your Context7 API key

**Note:** Installed via npx, no additional setup required

### deepwiki

**Purpose:** Access DeepWiki documentation

**Bridge Location:** `C:\Users\%USERNAME%\.config\opencode\deepwiki-bridge\bridge.py`

**Requirements:**
- Python 3
- requests library (`pip install requests`)

### tavily

**Purpose:** Web search via Tavily API

**Environment:**
- `TAVILY_API_KEY`: Your Tavily API key

**Note:** Installed via npx, no additional setup required

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

1. **Increase timeout values** in `opencode.jsonc`:
   ```json
   "timeout": 45000
   ```

2. **Check network connectivity** for API-based MCPs (context7, tavily)

3. **Verify Chrome is running** for chrome-devtools MCP

### Chrome DevTools Connection Failed

1. Ensure Chrome is launched with remote debugging:
   ```powershell
   curl http://127.0.0.1:9333/json/version
   ```

2. Check that the profile path is correct in the config

3. Try a different port if 9333 is in use

### Skills Not Loading

1. Verify skills are in the correct directory:
   ```powershell
   ls "$env:USERPROFILE\.config\opencode\skills"
   ```

2. Check that each skill has a `SKILL.md` file

3. Restart OpenCode Desktop

## Migration from WSL

This setup was migrated from WSL Ubuntu to Windows. Key changes:

- **Paths**: WSL paths (`/home/vic/...`) → Windows paths (`C:\Users\...`)
- **Chrome Profile**: WSL Chrome → Windows Chrome
- **Node**: WSL node → Windows node
- **Python**: WSL python3 → Windows python

## Contributing

Feel free to submit issues or PRs if you find bugs or want to add more skills.

## License

MIT