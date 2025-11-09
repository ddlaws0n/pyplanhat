"""Base resource class for API resources."""

from typing import Any, Dict

import httpx

from pyplanhat._exceptions import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
    ServerError,
)


class BaseResource:
    """Base class for all API resources."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """Handle HTTP response with proper error handling."""
        if response.status_code == 401 or response.status_code == 403:
            raise AuthenticationError(
                "Authentication failed", response.status_code, response.text
            )
        elif response.status_code == 404:
            raise InvalidRequestError(
                "Resource not found", response.status_code, response.text
            )
        elif response.status_code == 429:
            raise RateLimitError(
                "Rate limit exceeded", response.status_code, response.text
            )
        elif response.status_code >= 500:
            raise ServerError(
                f"Server error: {response.text}", response.status_code, response.text
            )
        elif response.status_code >= 400:
            raise APIError(
                f"API error: {response.text}", response.status_code, response.text
            )

        response.raise_for_status()
        return response.json()  # type: ignore[no-any-return]
