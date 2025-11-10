"""Pytest configuration and fixtures for tests."""

import pytest_asyncio

from pyplanhat._sync.client import PyPlanhat


@pytest_asyncio.fixture
def async_client() -> PyPlanhat:  # type: ignore[misc]
    """Fixture providing a PyPlanhat client for testing."""
    client = PyPlanhat(api_key="test-api-key", base_url="https://api.planhat.com")
    yield client
    client.close()
