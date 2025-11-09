# PyPlanhat SDK

Modern async-first Python SDK for the Planhat API.

## Features

- 🚀 **Async-first architecture** with auto-generated sync support
- 📦 **Built with modern Python tooling** (httpx, pydantic, uv)
- 🔒 **Type-safe** with full mypy support
- ✨ **Comprehensive error handling** with custom exception hierarchy
- 🧪 **Extensively tested** with 90%+ coverage

## Installation

```bash
pip install pyplanhat
```

## Quick Start

### Async Usage

```python
import asyncio
from pyplanhat import AsyncPyPlanhat

async def main():
    async with AsyncPyPlanhat(api_key="your-api-key") as client:
        # API calls here (Phase 1+)
        pass

asyncio.run(main())
```

### Sync Usage

```python
from pyplanhat import PyPlanhat

with PyPlanhat(api_key="your-api-key") as client:
    # API calls here (Phase 1+)
    pass
```

## Configuration

Set environment variables for convenient testing:

```bash
export PLANHAT_API_KEY="your-api-key"
export PLANHAT_API_BASE_URL="https://api.planhat.com"  # optional
```

Or pass directly to the client:

```python
client = AsyncPyPlanhat(
    api_key="your-api-key",
    base_url="https://api.planhat.com"
)
```

## Development

This project is currently in **Phase 0** development. The foundation is being built using a phased approach with OpenCode agents.

### Setup

```bash
# Clone repository
git clone https://github.com/your-username/pyplanhat.git
cd pyplanhat

# Install dependencies
uv sync --all-groups

# Run tests
uv run pytest -v

# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Type check
uv run mypy src/
```

### Architecture

PyPlanhat uses an **async-first DRY architecture**:

1. ✏️ Write async code in `src/pyplanhat/_async/`
2. 🔄 Generate sync code: `python scripts/generate_sync.py`
3. ✅ Both versions tested identically
4. 📦 Zero duplication of business logic

The synchronous version is automatically generated from the async source using `unasync`, ensuring perfect parity between both APIs.

### Development Guidelines

See [CLAUDE.md](CLAUDE.md) for detailed development guidelines and workflow.

Key principles:
- **Never edit** files in `_sync/` directories (they're auto-generated)
- **Always run** `python scripts/generate_sync.py` after modifying async code
- **Maintain test parity** between async and sync test suites
- **Follow the phased plan** in `docs/pyplanhat/PLAN.md`

### Project Structure

```
src/pyplanhat/
├── _async/              # Async source code (write here)
│   ├── client.py        # Main async client
│   └── resources/       # Async resource implementations
├── _sync/               # Generated sync code (never edit)
│   ├── client.py        # Generated sync client
│   └── resources/       # Generated sync resources
├── _exceptions.py       # Custom exception hierarchy
└── __init__.py         # Public API exports

tests/
├── _async/             # Async tests (write here)
└── _sync/              # Generated sync tests (never edit)
```

## Roadmap

- **Phase 0**: Foundation (exception hierarchy, client shell, code generation) ✅ **In Progress**
- **Phase 1**: Companies resource implementation
- **Phase 2**: EndUsers and Conversations resources
- **Phase 3**: Documentation (mkdocs, API reference)
- **Phase 4**: Release to PyPI

## Contributing

This project follows strict architectural patterns and phased development. Please review:

1. [CLAUDE.md](CLAUDE.md) - Development workflow and commands
2. [docs/pyplanhat/PLAN.md](docs/pyplanhat/PLAN.md) - Phased development plan
3. [docs/pyplanhat/ARCHITECTURE.md](docs/pyplanhat/ARCHITECTURE.md) - Architecture details

## License

MIT License - see [LICENSE](LICENSE) for details.

## Support

For issues, questions, or contributions, please open an issue on GitHub.
