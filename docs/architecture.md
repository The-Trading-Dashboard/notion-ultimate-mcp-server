# Architecture Overview

## System Design

### Core Components

```
┌─────────────────────────────────────────────────────────┐
│                   Claude Desktop                        │
│                 (MCP Client)                            │
└────────────────────┬────────────────────────────────────┘
                     │ MCP Protocol
                     ↓
┌─────────────────────────────────────────────────────────┐
│              MCP Server (Python)                        │
├─────────────────────────────────────────────────────────┤
│  Resources  │  Tools  │  Prompts                        │
│  (20+)      │  (30+)  │  (15+)                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│                Core Business Logic                      │
├─────────────────────────────────────────────────────────┤
│  NotionAPI  │  TaskAnalyzer  │  Config                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────┐
│                  Notion API                             │
│              (External Service)                         │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

#### Continuous AI Workflow

1. **User initiates**: "What should I work on next?"
2. **Claude calls**: `get_next_task` tool via MCP
3. **Server fetches**: Tasks from Notion API
4. **TaskAnalyzer**: Selects best task based on:
   - Dependencies (unblocked)
   - Energy level (matches current state)
   - Sprint priority
   - Estimated hours (fits available time)
5. **Server returns**: Task context to Claude
6. **Claude generates**: AI-optimized prompt using `generate_ai_prompt`
7. **User completes**: Task work
8. **Claude calls**: `mark_complete` tool
9. **Server updates**: Task status, unblocks dependencies
10. **Loop continues**: Back to step 2

### Key Design Decisions

#### Why MCP?
- **Native Claude integration**: No API wrappers needed
- **Stateless**: Server doesn't maintain session state
- **Extensible**: Easy to add new tools/resources
- **Type-safe**: Schema validation built-in

#### Why Core Separation?
- **Reusability**: Core logic usable in CLI scripts and MCP server
- **Testability**: Can test business logic independently
- **Maintainability**: Clear separation of concerns

#### Why Not Just Scripts?
- **Manual orchestration**: Scripts require manual task selection
- **No AI context**: Scripts don't understand AI workflow
- **Stateful**: Scripts maintain state, harder to integrate

### Performance Considerations

- **API Rate Limiting**: 3 requests/second (Notion limit)
- **Caching**: 5-minute TTL for task list
- **Pagination**: Fetch 100 items per page
- **Retries**: 3 attempts with exponential backoff

### Security

- **Token storage**: Environment variables only
- **No logging**: API tokens never logged
- **Read-only resources**: Resources never modify data
- **Tool validation**: All inputs validated against schema

## Next Steps

- [MCP Implementation Guide](mcp-guide.md)
- [Notion Setup Guide](notion-setup.md)
- [API Reference](api-reference.md)