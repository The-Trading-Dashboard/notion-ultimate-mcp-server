# Notion Setup Guide

## Database Requirements

### Required Properties

Your Notion database must have these properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| Task | Title | ✅ Yes | Task name |
| Status | Select | ✅ Yes | Not Started, In Progress, Blocked, Completed |
| Category | Select | ✅ Yes | Task category (ML/AI, Security, etc.) |
| Est Hours | Number | ✅ Yes | Estimated hours |
| Energy Required | Select | ✅ Yes | Low, Medium, High |
| Priority | Select | ✅ Yes | Low, Medium, High, Critical |
| Dependencies | Relation | ✅ Yes | Self-relation for dependencies |
| Blocks | Relation | ✅ Yes | Self-relation for blocking |
| Task ID | Text | ✅ Yes | Unique identifier |
| Sprint | Select | ⚠️ Recommended | Sprint assignment |
| Phase | Select | ⚠️ Recommended | Project phase |
| Actual Hours | Number | ⚠️ Recommended | Time tracking |
| Health Score | Formula | ✅ Yes | Task health indicator |

### Optional Properties

| Property | Type | Description |
|----------|------|-------------|
| Notes | Text | Additional context |
| Tags | Multi-select | Flexible categorization |
| Due Date | Date | Deadline |
| Assignee | Person | Team member |
| Created At | Created time | Automatic |
| Updated At | Last edited time | Automatic |

## Setting Up Integration

### 1. Create Notion Integration

1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Name it: **"Trading System MCP Server"**
4. Select your workspace
5. Capabilities needed:
   - ✅ Read content
   - ✅ Update content
   - ✅ Insert content
6. Click **"Submit"**
7. Copy the **Internal Integration Token**

### 2. Connect Integration to Database

1. Open your Task Tracker database in Notion
2. Click **"..."** (top right)
3. Scroll down to **"Connections"**
4. Click **"+ Add connections"**
5. Select **"Trading System MCP Server"**
6. Click **"Confirm"**

### 3. Get Database ID

Your database URL looks like:
```
https://notion.so/your-workspace/8dc1f9d6abb64e7f9c5d52541e3aaca4?v=...
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                  This is your database ID
```

Or the clean URL:
```
https://notion.so/8dc1f9d6abb64e7f9c5d52541e3aaca4
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

### 4. Configure Environment

Create `.env` file:
```bash
NOTION_TOKEN=secret_abc123...
DATABASE_ID=8dc1f9d6abb64e7f9c5d52541e3aaca4
```

## Formula Reference

### Health Score Formula

```javascript
if(prop("Status") == "Completed", 100,
  if(prop("Status") == "Blocked", 0,
    if(empty(prop("Dependencies")), 80,
      if(prop("Dependencies").filter(current.prop("Status") != "Completed").length() == 0, 90,
        50
      )
    )
  )
)
```

### Days Until Due

```javascript
if(empty(prop("Due Date")), empty(),
  dateBetween(prop("Due Date"), now(), "days")
)
```

## Testing Your Setup

```bash
# Test API connection
python -c "from core.config import Config; from core.notion_api import NotionAPI; config = Config.from_env(); api = NotionAPI(config); print('✅ Connection successful')"

# Test task fetching
python -m scripts.task_manager --test
```

## Troubleshooting

### "Invalid token" Error
- Verify token in `.env` matches integration token
- Check token doesn't have extra spaces
- Ensure integration is connected to database

### "Database not found" Error
- Verify database ID is correct (32 characters)
- Check integration has permission to access database
- Ensure database isn't in trash

### Missing Properties
- Required properties must exist before running
- Property names are case-sensitive
- Use exact names from this guide

## Next Steps

- [Architecture Overview](architecture.md)
- [MCP Implementation Guide](mcp-guide.md)