# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import get_team_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.get_team_list_response import GetTeamListResponse

__all__ = ["GetTeamsResource", "AsyncGetTeamsResource"]


class GetTeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GetTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return GetTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GetTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#with_streaming_response
        """
        return GetTeamsResourceWithStreamingResponse(self)

    def list(
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
        id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetTeamListResponse:
        """
        Args:
          hl: This is the locale or language code using
              [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
              [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          id: The team slug(s).

              You can input more than one slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/getTeams"
            if self._client._base_url_overridden
            else "https://esports-api.lolesports.com/persisted/gw/getTeams",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hl": hl,
                        "id": id,
                    },
                    get_team_list_params.GetTeamListParams,
                ),
            ),
            cast_to=GetTeamListResponse,
        )


class AsyncGetTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGetTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGetTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGetTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Atelier-Nayr/lolesports_api-python#with_streaming_response
        """
        return AsyncGetTeamsResourceWithStreamingResponse(self)

    async def list(
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
        id: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetTeamListResponse:
        """
        Args:
          hl: This is the locale or language code using
              [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
              [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

          id: The team slug(s).

              You can input more than one slug.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/getTeams"
            if self._client._base_url_overridden
            else "https://esports-api.lolesports.com/persisted/gw/getTeams",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "hl": hl,
                        "id": id,
                    },
                    get_team_list_params.GetTeamListParams,
                ),
            ),
            cast_to=GetTeamListResponse,
        )


class GetTeamsResourceWithRawResponse:
    def __init__(self, get_teams: GetTeamsResource) -> None:
        self._get_teams = get_teams

        self.list = to_raw_response_wrapper(
            get_teams.list,
        )


class AsyncGetTeamsResourceWithRawResponse:
    def __init__(self, get_teams: AsyncGetTeamsResource) -> None:
        self._get_teams = get_teams

        self.list = async_to_raw_response_wrapper(
            get_teams.list,
        )


class GetTeamsResourceWithStreamingResponse:
    def __init__(self, get_teams: GetTeamsResource) -> None:
        self._get_teams = get_teams

        self.list = to_streamed_response_wrapper(
            get_teams.list,
        )


class AsyncGetTeamsResourceWithStreamingResponse:
    def __init__(self, get_teams: AsyncGetTeamsResource) -> None:
        self._get_teams = get_teams

        self.list = async_to_streamed_response_wrapper(
            get_teams.list,
        )
