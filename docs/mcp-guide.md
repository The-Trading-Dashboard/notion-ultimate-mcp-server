# MCP Implementation Guide

## What is MCP?

The **Model Context Protocol (MCP)** is an open protocol that enables AI assistants like Claude to:
- Access external data sources (Resources)
- Execute operations (Tools)
- Use pre-defined templates (Prompts)

## Our Implementation

### Resources (Read-Only State)

Resources provide read-only access to system state:

| URI | Description | Returns |
|-----|-------------|----------|
| `notion://tasks/next` | Next recommended task | Task object with full context |
| `notion://tasks/current` | Current in-progress tasks | List of tasks |
| `notion://sprint/current` | Current sprint status | Sprint progress and velocity |
| `notion://analytics/velocity` | Velocity metrics | Historical performance data |
| `notion://dependencies/{id}` | Task dependency tree | Graph of dependencies |

**Example Usage in Claude:**
```
User: "Show me my current sprint progress"
Claude: [Reads notion://sprint/current resource]
Claude: "Sprint 1 is 60% complete. You've finished 6/10 tasks..."
```

### Tools (Executable Operations)

Tools allow Claude to execute operations:

| Tool | Description | Parameters |
|------|-------------|------------|
| `get_next_task` | Get next recommended task | energy_level, available_hours |
| `mark_complete` | Complete task, unblock dependencies | task_id, actual_hours |
| `search_tasks` | Search and filter tasks | query, status, category |
| `create_task` | Create new task | title, category, est_hours, etc. |
| `update_task` | Update task properties | task_id, properties |
| `plan_sprint` | Plan sprint with capacity | sprint_name, capacity_hours |
| `analyze_dependencies` | Analyze dependency graph | None |

**Example Usage in Claude:**
```
User: "What should I work on next? I have 2 hours and medium energy"
Claude: [Calls get_next_task tool with energy_level="medium", available_hours=2]
Claude: "Work on 'Build user authentication' (2 hours, medium energy)..."
```

### Prompts (AI-Optimized Templates)

Prompts provide AI-optimized templates:

| Prompt | Description | Arguments |
|--------|-------------|----------|
| `generate_ai_prompt` | Generate task-specific prompt | task_id |
| `continuous_workflow` | Enable autonomous coding | None |
| `debug_assistant` | Generate debugging prompts | task_id, error_context |
| `code_review` | Generate code review prompts | task_id, code_changes |
| `testing_strategy` | Generate testing prompts | task_id |

**Example Usage in Claude:**
```
User: "Generate a prompt for my current task"
Claude: [Uses generate_ai_prompt with current task ID]
Claude: [Returns detailed prompt with context, examples, constraints]
```

## Continuous AI Workflow

The killer feature - autonomous task orchestration:

```
1. User: "Start continuous workflow"
   ↓
2. Claude: [Calls get_next_task]
   ↓
3. Claude: "Work on: Build user auth (2 hrs, medium energy)"
   ↓
4. Claude: [Uses generate_ai_prompt for that task]
   ↓
5. Claude: [Generates detailed prompt with context]
   ↓
6. User: [Works on task]
   ↓
7. User: "Done, next task"
   ↓
8. Claude: [Calls mark_complete, then get_next_task]
   ↓
9. Claude: "Great! Next: Add password hashing (1.5 hrs, low energy)"
   ↓
10. Loop continues indefinitely!
```

## Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or equivalent:

```json
{
  "mcpServers": {
    "notion-ultimate": {
      "command": "python",
      "args": [
        "-m",
        "mcp.server"
      ],
      "cwd": "/path/to/notion-ultimate-mcp-server",
      "env": {
        "NOTION_TOKEN": "secret_abc123...",
        "DATABASE_ID": "8dc1f9d6abb64e7f9c5d52541e3aaca4"
      }
    }
  }
}
```

## Testing MCP Server

### 1. Test Server Startup
```bash
python -m mcp.server
```

Should output:
```
INFO:__main__:Notion Ultimate MCP Server starting...
```

### 2. Test with MCP Inspector
```bash
# Install MCP Inspector
npm install -g @modelcontextprotocol/inspector

# Run inspector
mcp-inspector python -m mcp.server
```

### 3. Test in Claude Desktop

1. Restart Claude Desktop after config change
2. Look for hammer icon (🔨) in input box
3. Try: "What tools do you have available?"
4. Claude should list Notion tools

## Debugging

### Server Logs

Logs go to `notion_mcp.log`:
```bash
tail -f notion_mcp.log
```

### Enable Debug Mode

In `.env`:
```bash
DEBUG=true
MCP_LOG_LEVEL=DEBUG
```

### Common Issues

**Claude doesn't see tools:**
- Check `claude_desktop_config.json` syntax
- Verify paths are absolute, not relative
- Restart Claude Desktop completely

**Server crashes immediately:**
- Check `.env` has valid tokens
- Verify Python 3.11+ installed
- Check `requirements.txt` installed

**Tools timeout:**
- Notion API may be slow
- Check network connection
- Increase timeout in config

## Next Steps

- [Architecture Overview](architecture.md)
- [Notion Setup Guide](notion-setup.md)
- [API Reference](api-reference.md)