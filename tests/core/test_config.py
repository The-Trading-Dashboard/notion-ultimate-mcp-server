"""Tests for configuration management."""

import pytest
import os
from core.config import Config


def test_config_from_env():
    """Test loading config from environment."""
    # Set test environment variables
    os.environ["NOTION_TOKEN"] = "test_token_123"
    os.environ["DATABASE_ID"] = "test_db_123"
    
    config = Config.from_env()
    
    assert config.notion_token == "test_token_123"
    assert config.database_id == "test_db_123"
    assert config.mcp_port == 3000  # Default value
    

def test_config_missing_required():
    """Test config fails without required variables."""
    # Clear environment variables
    os.environ.pop("NOTION_TOKEN", None)
    os.environ.pop("DATABASE_ID", None)
    
    with pytest.raises(ValueError):
        Config.from_env()


def test_notion_headers():
    """Test Notion API headers generation."""
    config = Config(
        notion_token="test_token",
        database_id="test_db"
    )
    
    headers = config.notion_headers
    
    assert "Authorization" in headers
    assert "Bearer test_token" in headers["Authorization"]
    assert headers["Notion-Version"] == "2022-06-28"
    assert headers["Content-Type"] == "application/json"