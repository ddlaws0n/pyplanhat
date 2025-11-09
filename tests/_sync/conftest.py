"""Pytest configuration and fixtures for sync tests."""

import pytest

from pyplanhat._sync.client import PyPlanhat


@pytest.fixture
def sync_client() -> PyPlanhat:  # type: ignore[misc]
    """Fixture providing a sync PyPlanhat client for testing."""
    client = PyPlanhat(api_key="test-api-key", base_url="https://api.planhat.com")
    yield client
    client.close()
