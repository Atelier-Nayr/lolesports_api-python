# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import window_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.window_retrieve_response import WindowRetrieveResponse

__all__ = ["WindowResource", "AsyncWindowResource"]


class WindowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WindowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return WindowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WindowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return WindowResourceWithStreamingResponse(self)

    def retrieve(
        self,
        game_id: int,
        *,
        starting_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WindowRetrieveResponse:
        """
        Args:
          starting_time: The date-time (RFC3339)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/window/{game_id}"
            if self._client._base_url_overridden
            else f"https://feed.lolesports.com/livestats/v1/window/{game_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"starting_time": starting_time}, window_retrieve_params.WindowRetrieveParams),
            ),
            cast_to=WindowRetrieveResponse,
        )


class AsyncWindowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWindowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWindowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWindowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return AsyncWindowResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        game_id: int,
        *,
        starting_time: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WindowRetrieveResponse:
        """
        Args:
          starting_time: The date-time (RFC3339)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/window/{game_id}"
            if self._client._base_url_overridden
            else f"https://feed.lolesports.com/livestats/v1/window/{game_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"starting_time": starting_time}, window_retrieve_params.WindowRetrieveParams
                ),
            ),
            cast_to=WindowRetrieveResponse,
        )


class WindowResourceWithRawResponse:
    def __init__(self, window: WindowResource) -> None:
        self._window = window

        self.retrieve = to_raw_response_wrapper(
            window.retrieve,
        )


class AsyncWindowResourceWithRawResponse:
    def __init__(self, window: AsyncWindowResource) -> None:
        self._window = window

        self.retrieve = async_to_raw_response_wrapper(
            window.retrieve,
        )


class WindowResourceWithStreamingResponse:
    def __init__(self, window: WindowResource) -> None:
        self._window = window

        self.retrieve = to_streamed_response_wrapper(
            window.retrieve,
        )


class AsyncWindowResourceWithStreamingResponse:
    def __init__(self, window: AsyncWindowResource) -> None:
        self._window = window

        self.retrieve = async_to_streamed_response_wrapper(
            window.retrieve,
        )
