"""Setup configuration for Notion Ultimate MCP Server."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="notion-ultimate-mcp-server",
    version="0.1.0",
    author="The Trading Dashboard",
    description="Revolutionary MCP-enabled Notion task management system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/The-Trading-Dashboard/notion-ultimate-mcp-server",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.11",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "mcp>=0.9.0",
        "pandas>=2.0.0",
        "python-dateutil>=2.8.2",
        "click>=8.1.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "notion-mcp-server=mcp.server:main",
            "notion-task-manager=scripts.task_manager:main",
            "notion-bulk-updater=scripts.bulk_updater:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Groupware",
    ],
)