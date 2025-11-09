"""Async client for Planhat API."""

import os
from typing import Optional

import httpx


class AsyncPyPlanhat:
    """Async client for Planhat API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        self.api_key = api_key or os.getenv("PLANHAT_API_KEY")
        self.base_url = (
            base_url or os.getenv("PLANHAT_API_BASE_URL", "https://api.planhat.com")
        ).rstrip("/")

        if not self.api_key:
            raise ValueError(
                "API key required. Set PLANHAT_API_KEY environment variable "
                "or pass api_key parameter."
            )

        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=30.0,
        )

    async def __aenter__(self) -> "AsyncPyPlanhat":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore[no-untyped-def]
        await self.close()

    async def close(self) -> None:
        """Close the HTTP client."""
        await self._client.aclose()
