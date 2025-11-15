# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import get_schedule_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
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
from ..types.get_schedule_retrieve_response import GetScheduleRetrieveResponse

__all__ = ["GetScheduleResource", "AsyncGetScheduleResource"]


class GetScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GetScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return GetScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GetScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return GetScheduleResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        hl: Literal[
            "en-US",
            "en-GB",
            "en-AU",
            "cs-CZ",
            "de-DE",
            "el-GR",
            "es-ES",
            "es-MX",
            "fr-FR",
            "hu-HU",
            "it-IT",
            "pl-PL",
            "pt-BR",
            "ro-RO",
            "ru-RU",
            "tr-TR",
            "ja-JP",
            "ko-KR",
        ],
        league_id: Iterable[int] | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetScheduleRetrieveResponse:
        """
        Args:
          hl: This is the locale or language code using
              [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
              [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          league_id: The id(s) of the league(s) you want details of

          page_token: Base 64 encoded string used to determine the next "page" of data to pull

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/getSchedule"
            if self._client._base_url_overridden
            else "https://esports-api.lolesports.com/persisted/gw/getSchedule",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hl": hl,
                        "league_id": league_id,
                        "page_token": page_token,
                    },
                    get_schedule_retrieve_params.GetScheduleRetrieveParams,
                ),
            ),
            cast_to=GetScheduleRetrieveResponse,
        )


class AsyncGetScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGetScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGetScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGetScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return AsyncGetScheduleResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        hl: Literal[
            "en-US",
            "en-GB",
            "en-AU",
            "cs-CZ",
            "de-DE",
            "el-GR",
            "es-ES",
            "es-MX",
            "fr-FR",
            "hu-HU",
            "it-IT",
            "pl-PL",
            "pt-BR",
            "ro-RO",
            "ru-RU",
            "tr-TR",
            "ja-JP",
            "ko-KR",
        ],
        league_id: Iterable[int] | Omit = omit,
        page_token: Union[str, Base64FileInput] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetScheduleRetrieveResponse:
        """
        Args:
          hl: This is the locale or language code using
              [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
              [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          league_id: The id(s) of the league(s) you want details of

          page_token: Base 64 encoded string used to determine the next "page" of data to pull

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/getSchedule"
            if self._client._base_url_overridden
            else "https://esports-api.lolesports.com/persisted/gw/getSchedule",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "hl": hl,
                        "league_id": league_id,
                        "page_token": page_token,
                    },
                    get_schedule_retrieve_params.GetScheduleRetrieveParams,
                ),
            ),
            cast_to=GetScheduleRetrieveResponse,
        )


class GetScheduleResourceWithRawResponse:
    def __init__(self, get_schedule: GetScheduleResource) -> None:
        self._get_schedule = get_schedule

        self.retrieve = to_raw_response_wrapper(
            get_schedule.retrieve,
        )


class AsyncGetScheduleResourceWithRawResponse:
    def __init__(self, get_schedule: AsyncGetScheduleResource) -> None:
        self._get_schedule = get_schedule

        self.retrieve = async_to_raw_response_wrapper(
            get_schedule.retrieve,
        )


class GetScheduleResourceWithStreamingResponse:
    def __init__(self, get_schedule: GetScheduleResource) -> None:
        self._get_schedule = get_schedule

        self.retrieve = to_streamed_response_wrapper(
            get_schedule.retrieve,
        )


class AsyncGetScheduleResourceWithStreamingResponse:
    def __init__(self, get_schedule: AsyncGetScheduleResource) -> None:
        self._get_schedule = get_schedule

        self.retrieve = async_to_streamed_response_wrapper(
            get_schedule.retrieve,
        )
