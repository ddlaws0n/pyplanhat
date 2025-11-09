# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PyPlanhat SDK is a modern Python SDK for the Planhat API with async-first architecture. The project uses `unasync` to automatically generate synchronous code from async source, ensuring zero duplication of business logic.

## Development Commands

### Setup
```bash
# Install dependencies
uv sync --extra dev --extra test

# Install dependencies without resolving (if lockfile unchanged)
uv sync --frozen --extra dev --extra test
```

### Testing
```bash
# Run all tests
uv run pytest -v

# Run with coverage
uv run pytest --cov=src/pyplanhat --cov-report=term-missing

# Run specific test file
uv run pytest tests/_async/test_companies.py -v

# Run async tests only
uv run pytest tests/_async/ -v

# Run sync tests only
uv run pytest tests/_sync/ -v
```

### Code Quality
```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Auto-fix linting issues
uv run ruff check . --fix

# Type checking
uv run mypy src/
```

### Code Generation
```bash
# Regenerate sync code from async source (MUST run after any async code changes)
python scripts/generate_sync.py

# Format and fix generated code
uv run ruff format src/pyplanhat/_sync/ tests/_sync/
uv run ruff check src/pyplanhat/_sync/ tests/_sync/ --fix
```

### Build and Release
```bash
# Build package
uv build

# Check package
uv run twine check dist/*
```

## Architecture Principles

### 1. Async-First DRY Architecture

**CRITICAL**: All source code must be written in `src/pyplanhat/_async/` and `tests/_async/` directories. The synchronous versions in `_sync/` directories are **auto-generated** and must **NEVER** be edited manually.

**Workflow**:
1. Write/modify code in `_async/` directories
2. Run `python scripts/generate_sync.py` to regenerate sync code
3. Format and fix generated code with ruff
4. Commit both async source and generated sync code

### 2. Exception Hierarchy

Located in `src/pyplanhat/_exceptions.py`:
- `PyPlanhatError`: Base exception for all errors
- `APIConnectionError`: Network/timeout issues
- `APIError`: Base for HTTP errors (has `status_code` and `response_body` attributes)
  - `AuthenticationError`: 401/403 errors
  - `InvalidRequestError`: 400/404 errors
  - `RateLimitError`: 429 errors
  - `ServerError`: 5xx errors

### 3. Resource Implementation Pattern

Each resource (Companies, EndUsers, Conversations) follows this pattern:
- Inherits from `BaseResource`
- Located in `src/pyplanhat/_async/resources/`
- Implements standard CRUD operations: `list()`, `get()`, `create()`, `update()`, `delete()`
- Uses Pydantic models for data validation
- HTTP responses handled via `_handle_response()` method with proper error mapping

### 4. Client Architecture

The `AsyncPyPlanhat` client:
- Uses `httpx.AsyncClient` for HTTP operations
- Initializes resource namespaces (e.g., `client.companies`, `client.endusers`)
- Supports context manager pattern (`async with`)
- Handles authentication via Bearer token in headers

## Project Structure

```
src/pyplanhat/
├── _async/              # Async source code (WRITE HERE ONLY)
│   ├── client.py        # Main async client
│   └── resources/       # Async resource implementations
├── _sync/               # Generated sync code (NEVER EDIT)
│   ├── client.py        # Generated sync client
│   └── resources/       # Generated sync resources
├── _exceptions.py       # Custom exception hierarchy
└── __init__.py         # Public API exports

tests/
├── _async/             # Async tests (WRITE HERE ONLY)
└── _sync/              # Generated sync tests (NEVER EDIT)

docs/pyplanhat/
├── PLAN.md            # Development plan with phase breakdown
├── ARCHITECTURE.md    # Detailed architecture documentation
└── DEVELOPMENT.md     # Development workflow guide
```

## Development Workflow

### When Adding New Features

1. **Write async implementation** in `src/pyplanhat/_async/`
2. **Write async tests** in `tests/_async/`
3. **Regenerate sync code**: `python scripts/generate_sync.py`
4. **Format generated code**: `uv run ruff format src/pyplanhat/_sync/ tests/_sync/`
5. **Run all tests**: `uv run pytest -v`
6. **Verify type checking**: `uv run mypy src/`
7. **Commit both async and generated sync code**

### Quality Gates (Required Before Committing)

- [ ] All tests pass (both async and sync)
- [ ] `ruff check .` shows no issues
- [ ] `ruff format --check .` passes
- [ ] `mypy src/` passes without errors
- [ ] Sync code regenerated and committed
- [ ] Test coverage maintained

## Phased Development

The project follows a strict phase-based development plan (see `docs/pyplanhat/PLAN.md`):

- **Phase 0**: Foundation (P0-0 to P0-9) - Core infrastructure
- **Phase 1**: Companies (P1-1 to P1-5) - First resource implementation
- **Phase 2**: Resources (P2-1 to P2-3) - EndUsers and Conversations
- **Phase 3**: Documentation (P3-1 to P3-5) - mkdocs and API reference
- **Phase 4**: Release (P4-1 to P4-3) - PyPI publication

Each phase must be completed before moving to the next. No scope creep beyond documented tasks.

## Critical Rules

1. **NEVER edit files in `_sync/` directories** - they are auto-generated
2. **ALWAYS run `python scripts/generate_sync.py`** after modifying async code
3. **ALWAYS commit generated sync code** alongside async source code
4. **MAINTAIN test parity** between async and sync test suites
5. **NO business logic in `__init__.py`** - use for exports only
6. **USE Pydantic models** for all API data structures
7. **PRESERVE error context** - include status_code and response_body in exceptions
8. **FOLLOW the phased plan** - no features outside documented scope

## Testing Guidelines

- Use `pytest` with `pytest-asyncio` for async tests
- Use `responses` or `httpx_mock` for HTTP mocking
- Test happy path AND all error scenarios (400, 401, 403, 404, 429, 5xx)
- Maintain 90%+ test coverage
- Ensure async and sync tests are structurally identical (except async/await keywords)

## Configuration

- **Python**: 3.12+ required (configured in pyproject.toml)
- **Package Manager**: `uv` (Astral stack)
- **Linter/Formatter**: `ruff` (line-length: 99)
- **Type Checker**: `mypy` (strict mode, disallow_untyped_defs)
- **Build Backend**: `hatchling`
- **Test Framework**: `pytest` with addopts="-q"
