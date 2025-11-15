# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import league_list_params
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
from ..types.league_list_response import LeagueListResponse

__all__ = ["LeaguesResource", "AsyncLeaguesResource"]


class LeaguesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LeaguesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return LeaguesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaguesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return LeaguesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        query: league_list_params.Query,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LeagueListResponse:
        """Args:
          query: 'This endpoint requires either the id or the slug to be passed.

        If both are
              present then only the first one will be considered.

              _Due to a limitation in the OpenApi specification it is not possible to show the
              mutual exclusive nature that the query parameters in this endpoint require. The
              schema below is as close as a representation I could get in expressing the
              nature of the query parameters._

              Check the examples below to help better understand the query parameters needed.

              **Example 1**

              `https://api.lolesports.com/api/v1/leagues?id=3`

              This will return the details for **LEC**.

              **Example 2**

              `https://api.lolesports.com/api/v1/leagues?slug=worlds`

              This will return the details for **Worlds**

              **Example 3**

              `https://api.lolesports.com/api/v1/leagues?id=3&slug=worlds`

              In such a scenario where both query parameters are used only the first will be
              considered, hence it will only return the details for **LEC**.

              **Example 4**

              `https://api.lolesports.com/api/v1/leagues`

              This is not valid. At least one of the two query parameters (id or slug) is
              required.'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/leagues" if self._client._base_url_overridden else "https://api.lolesports.com/api/v1/leagues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, league_list_params.LeagueListParams),
            ),
            cast_to=LeagueListResponse,
        )


class AsyncLeaguesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLeaguesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeaguesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaguesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/lolesports_api-python#with_streaming_response
        """
        return AsyncLeaguesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        query: league_list_params.Query,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LeagueListResponse:
        """Args:
          query: 'This endpoint requires either the id or the slug to be passed.

        If both are
              present then only the first one will be considered.

              _Due to a limitation in the OpenApi specification it is not possible to show the
              mutual exclusive nature that the query parameters in this endpoint require. The
              schema below is as close as a representation I could get in expressing the
              nature of the query parameters._

              Check the examples below to help better understand the query parameters needed.

              **Example 1**

              `https://api.lolesports.com/api/v1/leagues?id=3`

              This will return the details for **LEC**.

              **Example 2**

              `https://api.lolesports.com/api/v1/leagues?slug=worlds`

              This will return the details for **Worlds**

              **Example 3**

              `https://api.lolesports.com/api/v1/leagues?id=3&slug=worlds`

              In such a scenario where both query parameters are used only the first will be
              considered, hence it will only return the details for **LEC**.

              **Example 4**

              `https://api.lolesports.com/api/v1/leagues`

              This is not valid. At least one of the two query parameters (id or slug) is
              required.'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/leagues" if self._client._base_url_overridden else "https://api.lolesports.com/api/v1/leagues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, league_list_params.LeagueListParams),
            ),
            cast_to=LeagueListResponse,
        )


class LeaguesResourceWithRawResponse:
    def __init__(self, leagues: LeaguesResource) -> None:
        self._leagues = leagues

        self.list = to_raw_response_wrapper(
            leagues.list,
        )


class AsyncLeaguesResourceWithRawResponse:
    def __init__(self, leagues: AsyncLeaguesResource) -> None:
        self._leagues = leagues

        self.list = async_to_raw_response_wrapper(
            leagues.list,
        )


class LeaguesResourceWithStreamingResponse:
    def __init__(self, leagues: LeaguesResource) -> None:
        self._leagues = leagues

        self.list = to_streamed_response_wrapper(
            leagues.list,
        )


class AsyncLeaguesResourceWithStreamingResponse:
    def __init__(self, leagues: AsyncLeaguesResource) -> None:
        self._leagues = leagues

        self.list = async_to_streamed_response_wrapper(
            leagues.list,
        )
