# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import get_standing_retrieve_params
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
from ..types.get_standing_retrieve_response import GetStandingRetrieveResponse

__all__ = ["GetStandingsResource", "AsyncGetStandingsResource"]


class GetStandingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GetStandingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return GetStandingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GetStandingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return GetStandingsResourceWithStreamingResponse(self)

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
        tournament_id: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetStandingRetrieveResponse:
        """
        Args:
          hl: This is the locale or language code using
              [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
              [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          tournament_id: The id(s) of the tournament(s) you want details ofs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/getStandings"
            if self._client._base_url_overridden
            else "https://esports-api.lolesports.com/persisted/gw/getStandings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hl": hl,
                        "tournament_id": tournament_id,
                    },
                    get_standing_retrieve_params.GetStandingRetrieveParams,
                ),
            ),
            cast_to=GetStandingRetrieveResponse,
        )


class AsyncGetStandingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGetStandingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGetStandingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGetStandingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return AsyncGetStandingsResourceWithStreamingResponse(self)

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
        tournament_id: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetStandingRetrieveResponse:
        """
        Args:
          hl: This is the locale or language code using
              [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
              [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          tournament_id: The id(s) of the tournament(s) you want details ofs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/getStandings"
            if self._client._base_url_overridden
            else "https://esports-api.lolesports.com/persisted/gw/getStandings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "hl": hl,
                        "tournament_id": tournament_id,
                    },
                    get_standing_retrieve_params.GetStandingRetrieveParams,
                ),
            ),
            cast_to=GetStandingRetrieveResponse,
        )


class GetStandingsResourceWithRawResponse:
    def __init__(self, get_standings: GetStandingsResource) -> None:
        self._get_standings = get_standings

        self.retrieve = to_raw_response_wrapper(
            get_standings.retrieve,
        )


class AsyncGetStandingsResourceWithRawResponse:
    def __init__(self, get_standings: AsyncGetStandingsResource) -> None:
        self._get_standings = get_standings

        self.retrieve = async_to_raw_response_wrapper(
            get_standings.retrieve,
        )


class GetStandingsResourceWithStreamingResponse:
    def __init__(self, get_standings: GetStandingsResource) -> None:
        self._get_standings = get_standings

        self.retrieve = to_streamed_response_wrapper(
            get_standings.retrieve,
        )


class AsyncGetStandingsResourceWithStreamingResponse:
    def __init__(self, get_standings: AsyncGetStandingsResource) -> None:
        self._get_standings = get_standings

        self.retrieve = async_to_streamed_response_wrapper(
            get_standings.retrieve,
        )
