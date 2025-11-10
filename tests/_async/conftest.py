"""Pytest configuration and fixtures for tests."""

import pytest

from pyplanhat._async.client import AsyncPyPlanhat


@pytest.fixture
async def async_client() -> AsyncPyPlanhat:  # type: ignore[misc]
    """Fixture providing a PyPlanhat client for testing."""
    client = AsyncPyPlanhat(api_key="test-api-key", base_url="https://api.planhat.com")
    yield client
    await client.close()
