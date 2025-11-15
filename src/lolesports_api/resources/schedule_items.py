# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import schedule_item_list_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.schedule_item_list_response import ScheduleItemListResponse

__all__ = ["ScheduleItemsResource", "AsyncScheduleItemsResource"]


class ScheduleItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return ScheduleItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#with_streaming_response
        """
        return ScheduleItemsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        league_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleItemListResponse:
        """
        Args:
          league_id: The id of the league you want details of

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/scheduleItems"
            if self._client._base_url_overridden
            else "https://api.lolesports.com/api/v1/scheduleItems",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"league_id": league_id}, schedule_item_list_params.ScheduleItemListParams),
            ),
            cast_to=ScheduleItemListResponse,
        )


class AsyncScheduleItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#with_streaming_response
        """
        return AsyncScheduleItemsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        league_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleItemListResponse:
        """
        Args:
          league_id: The id of the league you want details of

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/scheduleItems"
            if self._client._base_url_overridden
            else "https://api.lolesports.com/api/v1/scheduleItems",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"league_id": league_id}, schedule_item_list_params.ScheduleItemListParams
                ),
            ),
            cast_to=ScheduleItemListResponse,
        )


class ScheduleItemsResourceWithRawResponse:
    def __init__(self, schedule_items: ScheduleItemsResource) -> None:
        self._schedule_items = schedule_items

        self.list = to_raw_response_wrapper(
            schedule_items.list,
        )


class AsyncScheduleItemsResourceWithRawResponse:
    def __init__(self, schedule_items: AsyncScheduleItemsResource) -> None:
        self._schedule_items = schedule_items

        self.list = async_to_raw_response_wrapper(
            schedule_items.list,
        )


class ScheduleItemsResourceWithStreamingResponse:
    def __init__(self, schedule_items: ScheduleItemsResource) -> None:
        self._schedule_items = schedule_items

        self.list = to_streamed_response_wrapper(
            schedule_items.list,
        )


class AsyncScheduleItemsResourceWithStreamingResponse:
    def __init__(self, schedule_items: AsyncScheduleItemsResource) -> None:
        self._schedule_items = schedule_items

        self.list = async_to_streamed_response_wrapper(
            schedule_items.list,
        )
