"""Pytest configuration and fixtures for async tests."""

import pytest

from pyplanhat._async.client import AsyncPyPlanhat


@pytest.fixture
async def async_client() -> AsyncPyPlanhat:  # type: ignore[misc]
    """Fixture providing an async PyPlanhat client for testing."""
    client = AsyncPyPlanhat(api_key="test-api-key", base_url="https://api.planhat.com")
    yield client
    await client.close()
