#!/usr/bin/env python3
"""Interactive task manager CLI.

This will be consolidated from notion_task_manager_enhanced.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.config import Config
from core.notion_api import NotionAPI


def main():
    """Main entry point."""
    print("🚀 Notion Task Manager")
    print("Implementation coming in Phase 1")
    
    # TODO: Consolidate from existing script
    # - Interactive menu
    # - Task operations
    # - Sprint management
    # - Analytics


if __name__ == "__main__":
    main()