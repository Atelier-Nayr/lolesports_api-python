# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import highlander_tournament_list_params
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
from ..types.highlander_tournament_list_response import HighlanderTournamentListResponse

__all__ = ["HighlanderTournamentsResource", "AsyncHighlanderTournamentsResource"]


class HighlanderTournamentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HighlanderTournamentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return HighlanderTournamentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HighlanderTournamentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return HighlanderTournamentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        league: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlanderTournamentListResponse:
        """
        If a league does not have highlanderTournament objects, the API will return 404

        Args:
          league: The id of the league you want details of

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/highlanderTournaments"
            if self._client._base_url_overridden
            else "https://api.lolesports.com/api/v2/highlanderTournaments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"league": league}, highlander_tournament_list_params.HighlanderTournamentListParams
                ),
            ),
            cast_to=HighlanderTournamentListResponse,
        )


class AsyncHighlanderTournamentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHighlanderTournamentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHighlanderTournamentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHighlanderTournamentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return AsyncHighlanderTournamentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        league: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlanderTournamentListResponse:
        """
        If a league does not have highlanderTournament objects, the API will return 404

        Args:
          league: The id of the league you want details of

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/highlanderTournaments"
            if self._client._base_url_overridden
            else "https://api.lolesports.com/api/v2/highlanderTournaments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"league": league}, highlander_tournament_list_params.HighlanderTournamentListParams
                ),
            ),
            cast_to=HighlanderTournamentListResponse,
        )


class HighlanderTournamentsResourceWithRawResponse:
    def __init__(self, highlander_tournaments: HighlanderTournamentsResource) -> None:
        self._highlander_tournaments = highlander_tournaments

        self.list = to_raw_response_wrapper(
            highlander_tournaments.list,
        )


class AsyncHighlanderTournamentsResourceWithRawResponse:
    def __init__(self, highlander_tournaments: AsyncHighlanderTournamentsResource) -> None:
        self._highlander_tournaments = highlander_tournaments

        self.list = async_to_raw_response_wrapper(
            highlander_tournaments.list,
        )


class HighlanderTournamentsResourceWithStreamingResponse:
    def __init__(self, highlander_tournaments: HighlanderTournamentsResource) -> None:
        self._highlander_tournaments = highlander_tournaments

        self.list = to_streamed_response_wrapper(
            highlander_tournaments.list,
        )


class AsyncHighlanderTournamentsResourceWithStreamingResponse:
    def __init__(self, highlander_tournaments: AsyncHighlanderTournamentsResource) -> None:
        self._highlander_tournaments = highlander_tournaments

        self.list = async_to_streamed_response_wrapper(
            highlander_tournaments.list,
        )
