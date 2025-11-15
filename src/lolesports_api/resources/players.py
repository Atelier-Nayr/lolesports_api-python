# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import player_list_params
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
from ..types.player_list_response import PlayerListResponse

__all__ = ["PlayersResource", "AsyncPlayersResource"]


class PlayersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return PlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return PlayersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        slug: str,
        tournament: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlayerListResponse:
        """
        If the `playerStatsSummaries` and `playerStatsHistories` keys are not present,
        then the player did not take part in that particular tournament.

        Args:
          slug: The player slug.

          tournament: The tournament ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/players" if self._client._base_url_overridden else "https://api.lolesports.com/api/v1/players",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "slug": slug,
                        "tournament": tournament,
                    },
                    player_list_params.PlayerListParams,
                ),
            ),
            cast_to=PlayerListResponse,
        )


class AsyncPlayersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return AsyncPlayersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        slug: str,
        tournament: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlayerListResponse:
        """
        If the `playerStatsSummaries` and `playerStatsHistories` keys are not present,
        then the player did not take part in that particular tournament.

        Args:
          slug: The player slug.

          tournament: The tournament ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/players" if self._client._base_url_overridden else "https://api.lolesports.com/api/v1/players",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "slug": slug,
                        "tournament": tournament,
                    },
                    player_list_params.PlayerListParams,
                ),
            ),
            cast_to=PlayerListResponse,
        )


class PlayersResourceWithRawResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.list = to_raw_response_wrapper(
            players.list,
        )


class AsyncPlayersResourceWithRawResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.list = async_to_raw_response_wrapper(
            players.list,
        )


class PlayersResourceWithStreamingResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.list = to_streamed_response_wrapper(
            players.list,
        )


class AsyncPlayersResourceWithStreamingResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.list = async_to_streamed_response_wrapper(
            players.list,
        )
