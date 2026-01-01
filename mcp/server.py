"""Main MCP server implementation.

This server exposes Notion task management capabilities to Claude Desktop
via the Model Context Protocol (MCP).
"""

import asyncio
import logging
from typing import Any, Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, Tool, Prompt, TextContent

from core.config import Config
from core.notion_api import NotionAPI
from core.task_analyzer import TaskAnalyzer

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NotionMCPServer:
    """MCP Server for Notion Ultimate Task Manager."""
    
    def __init__(self, config: Config):
        self.config = config
        self.notion_api = NotionAPI(config)
        self.server = Server("notion-ultimate")
        
        # Register handlers
        self._register_resources()
        self._register_tools()
        self._register_prompts()
    
    def _register_resources(self):
        """Register MCP resources."""
        
        @self.server.list_resources()
        async def list_resources() -> list[Resource]:
            """List available resources."""
            return [
                Resource(
                    uri="notion://tasks/next",
                    name="Next Recommended Task",
                    mimeType="application/json",
                    description="Get the next recommended task based on dependencies, energy, and priority"
                ),
                Resource(
                    uri="notion://tasks/current",
                    name="Current Tasks In Progress",
                    mimeType="application/json",
                    description="Get all tasks currently in progress"
                ),
                Resource(
                    uri="notion://sprint/current",
                    name="Current Sprint Status",
                    mimeType="application/json",
                    description="Get current sprint information and progress"
                ),
            ]
        
        @self.server.read_resource()
        async def read_resource(uri: str) -> str:
            """Read a specific resource."""
            # TODO: Implement resource reading
            logger.info(f"Reading resource: {uri}")
            return f"Resource content for {uri}"
    
    def _register_tools(self):
        """Register MCP tools."""
        
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            """List available tools."""
            return [
                Tool(
                    name="get_next_task",
                    description="Get the next recommended task based on context",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "energy_level": {
                                "type": "string",
                                "enum": ["low", "medium", "high"],
                                "description": "Current energy level"
                            },
                            "available_hours": {
                                "type": "number",
                                "description": "Hours available to work"
                            }
                        },
                        "required": ["energy_level", "available_hours"]
                    }
                ),
                Tool(
                    name="mark_complete",
                    description="Mark a task as complete and unblock dependencies",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "task_id": {
                                "type": "string",
                                "description": "ID of task to complete"
                            },
                            "actual_hours": {
                                "type": "number",
                                "description": "Actual hours spent"
                            }
                        },
                        "required": ["task_id"]
                    }
                ),
                Tool(
                    name="search_tasks",
                    description="Search tasks by various criteria",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query"
                            },
                            "status": {
                                "type": "string",
                                "enum": ["Not Started", "In Progress", "Blocked", "Completed"],
                                "description": "Filter by status"
                            },
                            "category": {
                                "type": "string",
                                "description": "Filter by category"
                            }
                        }
                    }
                ),
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
            """Execute a tool."""
            # TODO: Implement tool execution
            logger.info(f"Calling tool: {name} with args: {arguments}")
            return [TextContent(type="text", text=f"Tool {name} executed")]
    
    def _register_prompts(self):
        """Register MCP prompts."""
        
        @self.server.list_prompts()
        async def list_prompts() -> list[Prompt]:
            """List available prompts."""
            return [
                Prompt(
                    name="generate_ai_prompt",
                    description="Generate an AI-optimized prompt for a task",
                    arguments=[
                        {
                            "name": "task_id",
                            "description": "ID of the task",
                            "required": True
                        }
                    ]
                ),
                Prompt(
                    name="continuous_workflow",
                    description="Generate prompts for continuous AI workflow",
                    arguments=[]
                ),
            ]
        
        @self.server.get_prompt()
        async def get_prompt(name: str, arguments: dict[str, str]) -> str:
            """Get a specific prompt."""
            # TODO: Implement prompt generation
            logger.info(f"Getting prompt: {name} with args: {arguments}")
            return f"Prompt for {name}"
    
    async def run(self):
        """Run the MCP server."""
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Notion Ultimate MCP Server starting...")
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


async def main():
    """Main entry point."""
    try:
        config = Config.from_env()
        server = NotionMCPServer(config)
        await server.run()
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    asyncio.run(main())