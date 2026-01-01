"""Configuration management for Notion Ultimate MCP Server."""

import os
from typing import Optional
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration for Notion API and MCP server."""
    
    # Notion API
    notion_token: str
    database_id: str
    research_database_id: Optional[str] = None
    decisions_database_id: Optional[str] = None
    risks_database_id: Optional[str] = None
    
    # MCP Server
    mcp_port: int = 3000
    mcp_log_level: str = "INFO"
    
    # Feature Flags
    enable_auto_unblock: bool = True
    enable_ai_suggestions: bool = True
    enable_github_sync: bool = False
    
    # Performance
    api_rate_limit: int = 3
    cache_ttl: int = 300
    max_retries: int = 3
    
    # Development
    debug: bool = False
    log_file: str = "notion_mcp.log"
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        load_dotenv()
        
        notion_token = os.getenv("NOTION_TOKEN")
        database_id = os.getenv("DATABASE_ID")
        
        if not notion_token or not database_id:
            raise ValueError(
                "NOTION_TOKEN and DATABASE_ID must be set in environment variables"
            )
        
        return cls(
            notion_token=notion_token,
            database_id=database_id,
            research_database_id=os.getenv("RESEARCH_DATABASE_ID"),
            decisions_database_id=os.getenv("DECISIONS_DATABASE_ID"),
            risks_database_id=os.getenv("RISKS_DATABASE_ID"),
            mcp_port=int(os.getenv("MCP_PORT", "3000")),
            mcp_log_level=os.getenv("MCP_LOG_LEVEL", "INFO"),
            enable_auto_unblock=os.getenv("ENABLE_AUTO_UNBLOCK", "true").lower() == "true",
            enable_ai_suggestions=os.getenv("ENABLE_AI_SUGGESTIONS", "true").lower() == "true",
            enable_github_sync=os.getenv("ENABLE_GITHUB_SYNC", "false").lower() == "true",
            api_rate_limit=int(os.getenv("API_RATE_LIMIT", "3")),
            cache_ttl=int(os.getenv("CACHE_TTL", "300")),
            max_retries=int(os.getenv("MAX_RETRIES", "3")),
            debug=os.getenv("DEBUG", "false").lower() == "true",
            log_file=os.getenv("LOG_FILE", "notion_mcp.log"),
        )
    
    @property
    def notion_headers(self) -> dict:
        """Get headers for Notion API requests."""
        return {
            "Authorization": f"Bearer {self.notion_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }