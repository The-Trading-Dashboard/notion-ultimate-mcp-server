# Contributing to Notion Ultimate MCP Server

Thank you for your interest in contributing! This project is built for real-world trading system development with ADHD-friendly workflows.

## Development Setup

### 1. Clone and Install

```bash
git clone https://github.com/The-Trading-Dashboard/notion-ultimate-mcp-server.git
cd notion-ultimate-mcp-server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your Notion credentials
```

### 3. Run Tests

```bash
pytest tests/
```

## Project Structure

```
notion-ultimate-mcp-server/
├── core/           # Core business logic (reusable)
├── mcp/            # MCP server implementation
├── scripts/        # Standalone CLI tools
├── tests/          # Test suite
└── docs/           # Documentation
```

## Contribution Guidelines

### Code Style

- Use **Black** for formatting: `black .`
- Use **Flake8** for linting: `flake8 .`
- Use **MyPy** for type checking: `mypy core/ mcp/`
- Follow PEP 8 conventions

### Commit Messages

Format: `<type>: <description>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions/changes
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

Examples:
- `feat: Add get_next_task MCP tool`
- `fix: Handle missing dependencies in task analyzer`
- `docs: Update MCP setup guide`

### Pull Request Process

1. **Create feature branch**: `git checkout -b feat/your-feature`
2. **Make changes** with clear commits
3. **Add tests** for new functionality
4. **Update docs** if needed
5. **Run tests**: `pytest tests/`
6. **Format code**: `black . && flake8 .`
7. **Push branch**: `git push origin feat/your-feature`
8. **Open PR** with clear description

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Added tests
- [ ] All tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## Development Workflow

### Adding a New MCP Tool

1. **Define tool schema** in `mcp/tools/__init__.py`
2. **Implement tool logic** in `mcp/tools/your_tool.py`
3. **Register tool** in `mcp/server.py`
4. **Add tests** in `tests/mcp/test_your_tool.py`
5. **Update docs** in `docs/api-reference.md`

### Adding a New Core Feature

1. **Implement in core/** (e.g., `core/new_analyzer.py`)
2. **Add unit tests** in `tests/core/`
3. **Update exports** in `core/__init__.py`
4. **Use in MCP tools** or scripts
5. **Document** in `docs/architecture.md`

## Testing Guidelines

### Unit Tests

```python
# tests/core/test_notion_api.py
import pytest
from core.notion_api import NotionAPI
from core.config import Config

def test_fetch_tasks():
    config = Config.from_env()
    api = NotionAPI(config)
    tasks = api.fetch_all_tasks()
    assert isinstance(tasks, list)
```

### Integration Tests

```python
# tests/integration/test_mcp_workflow.py
import pytest
from mcp.server import NotionMCPServer

@pytest.mark.asyncio
async def test_continuous_workflow():
    # Test full autonomous workflow
    pass
```

### Running Specific Tests

```bash
# Run all tests
pytest

# Run specific file
pytest tests/core/test_notion_api.py

# Run with coverage
pytest --cov=core --cov=mcp

# Run only unit tests
pytest tests/core/

# Run only integration tests
pytest tests/integration/
```

## Documentation

- **Architecture changes**: Update `docs/architecture.md`
- **New MCP features**: Update `docs/mcp-guide.md`
- **Setup changes**: Update `docs/notion-setup.md`
- **API changes**: Update `docs/api-reference.md`

## Release Process

1. **Update version** in `setup.py` and `core/__init__.py`
2. **Update CHANGELOG.md** with changes
3. **Create release tag**: `git tag v0.2.0`
4. **Push tag**: `git push origin v0.2.0`
5. **Create GitHub release** with notes

## Questions?

Open an issue or discussion on GitHub!

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Celebrate successes

Thank you for contributing! 🚀