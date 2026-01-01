"""MCP Resources for task context and state.

Resources provide read-only access to system state:
- notion://tasks/next - Next recommended task
- notion://tasks/current - Current in-progress tasks
- notion://sprint/current - Current sprint status
- notion://analytics/velocity - Velocity metrics
- notion://dependencies/{task_id} - Task dependencies
"""

# Resource implementations coming in Phase 2