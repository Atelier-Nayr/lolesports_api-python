# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    teams,
    videos,
    window,
    details,
    leagues,
    players,
    get_live,
    get_games,
    get_teams,
    nav_items,
    get_leagues,
    get_schedule,
    get_standings,
    schedule_items,
    get_event_details,
    get_completed_events,
    highlander_tournaments,
    get_tournaments_for_league,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LolesportsAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "LolesportsAPI",
    "AsyncLolesportsAPI",
    "Client",
    "AsyncClient",
]


class LolesportsAPI(SyncAPIClient):
    get_leagues: get_leagues.GetLeaguesResource
    get_schedule: get_schedule.GetScheduleResource
    get_live: get_live.GetLiveResource
    get_tournaments_for_league: get_tournaments_for_league.GetTournamentsForLeagueResource
    get_standings: get_standings.GetStandingsResource
    get_completed_events: get_completed_events.GetCompletedEventsResource
    get_event_details: get_event_details.GetEventDetailsResource
    get_teams: get_teams.GetTeamsResource
    get_games: get_games.GetGamesResource
    window: window.WindowResource
    details: details.DetailsResource
    nav_items: nav_items.NavItemsResource
    videos: videos.VideosResource
    highlander_tournaments: highlander_tournaments.HighlanderTournamentsResource
    leagues: leagues.LeaguesResource
    schedule_items: schedule_items.ScheduleItemsResource
    teams: teams.TeamsResource
    players: players.PlayersResource
    with_raw_response: LolesportsAPIWithRawResponse
    with_streaming_response: LolesportsAPIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LolesportsAPI client instance.

        This automatically infers the `api_key` argument from the `LOLESPORTS_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LOLESPORTS_API_API_KEY")
        if api_key is None:
            raise LolesportsAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LOLESPORTS_API_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LOLESPORTS_API_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.get_leagues = get_leagues.GetLeaguesResource(self)
        self.get_schedule = get_schedule.GetScheduleResource(self)
        self.get_live = get_live.GetLiveResource(self)
        self.get_tournaments_for_league = get_tournaments_for_league.GetTournamentsForLeagueResource(self)
        self.get_standings = get_standings.GetStandingsResource(self)
        self.get_completed_events = get_completed_events.GetCompletedEventsResource(self)
        self.get_event_details = get_event_details.GetEventDetailsResource(self)
        self.get_teams = get_teams.GetTeamsResource(self)
        self.get_games = get_games.GetGamesResource(self)
        self.window = window.WindowResource(self)
        self.details = details.DetailsResource(self)
        self.nav_items = nav_items.NavItemsResource(self)
        self.videos = videos.VideosResource(self)
        self.highlander_tournaments = highlander_tournaments.HighlanderTournamentsResource(self)
        self.leagues = leagues.LeaguesResource(self)
        self.schedule_items = schedule_items.ScheduleItemsResource(self)
        self.teams = teams.TeamsResource(self)
        self.players = players.PlayersResource(self)
        self.with_raw_response = LolesportsAPIWithRawResponse(self)
        self.with_streaming_response = LolesportsAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLolesportsAPI(AsyncAPIClient):
    get_leagues: get_leagues.AsyncGetLeaguesResource
    get_schedule: get_schedule.AsyncGetScheduleResource
    get_live: get_live.AsyncGetLiveResource
    get_tournaments_for_league: get_tournaments_for_league.AsyncGetTournamentsForLeagueResource
    get_standings: get_standings.AsyncGetStandingsResource
    get_completed_events: get_completed_events.AsyncGetCompletedEventsResource
    get_event_details: get_event_details.AsyncGetEventDetailsResource
    get_teams: get_teams.AsyncGetTeamsResource
    get_games: get_games.AsyncGetGamesResource
    window: window.AsyncWindowResource
    details: details.AsyncDetailsResource
    nav_items: nav_items.AsyncNavItemsResource
    videos: videos.AsyncVideosResource
    highlander_tournaments: highlander_tournaments.AsyncHighlanderTournamentsResource
    leagues: leagues.AsyncLeaguesResource
    schedule_items: schedule_items.AsyncScheduleItemsResource
    teams: teams.AsyncTeamsResource
    players: players.AsyncPlayersResource
    with_raw_response: AsyncLolesportsAPIWithRawResponse
    with_streaming_response: AsyncLolesportsAPIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLolesportsAPI client instance.

        This automatically infers the `api_key` argument from the `LOLESPORTS_API_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("LOLESPORTS_API_API_KEY")
        if api_key is None:
            raise LolesportsAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the LOLESPORTS_API_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("LOLESPORTS_API_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.get_leagues = get_leagues.AsyncGetLeaguesResource(self)
        self.get_schedule = get_schedule.AsyncGetScheduleResource(self)
        self.get_live = get_live.AsyncGetLiveResource(self)
        self.get_tournaments_for_league = get_tournaments_for_league.AsyncGetTournamentsForLeagueResource(self)
        self.get_standings = get_standings.AsyncGetStandingsResource(self)
        self.get_completed_events = get_completed_events.AsyncGetCompletedEventsResource(self)
        self.get_event_details = get_event_details.AsyncGetEventDetailsResource(self)
        self.get_teams = get_teams.AsyncGetTeamsResource(self)
        self.get_games = get_games.AsyncGetGamesResource(self)
        self.window = window.AsyncWindowResource(self)
        self.details = details.AsyncDetailsResource(self)
        self.nav_items = nav_items.AsyncNavItemsResource(self)
        self.videos = videos.AsyncVideosResource(self)
        self.highlander_tournaments = highlander_tournaments.AsyncHighlanderTournamentsResource(self)
        self.leagues = leagues.AsyncLeaguesResource(self)
        self.schedule_items = schedule_items.AsyncScheduleItemsResource(self)
        self.teams = teams.AsyncTeamsResource(self)
        self.players = players.AsyncPlayersResource(self)
        self.with_raw_response = AsyncLolesportsAPIWithRawResponse(self)
        self.with_streaming_response = AsyncLolesportsAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LolesportsAPIWithRawResponse:
    def __init__(self, client: LolesportsAPI) -> None:
        self.get_leagues = get_leagues.GetLeaguesResourceWithRawResponse(client.get_leagues)
        self.get_schedule = get_schedule.GetScheduleResourceWithRawResponse(client.get_schedule)
        self.get_live = get_live.GetLiveResourceWithRawResponse(client.get_live)
        self.get_tournaments_for_league = get_tournaments_for_league.GetTournamentsForLeagueResourceWithRawResponse(
            client.get_tournaments_for_league
        )
        self.get_standings = get_standings.GetStandingsResourceWithRawResponse(client.get_standings)
        self.get_completed_events = get_completed_events.GetCompletedEventsResourceWithRawResponse(
            client.get_completed_events
        )
        self.get_event_details = get_event_details.GetEventDetailsResourceWithRawResponse(client.get_event_details)
        self.get_teams = get_teams.GetTeamsResourceWithRawResponse(client.get_teams)
        self.get_games = get_games.GetGamesResourceWithRawResponse(client.get_games)
        self.window = window.WindowResourceWithRawResponse(client.window)
        self.details = details.DetailsResourceWithRawResponse(client.details)
        self.nav_items = nav_items.NavItemsResourceWithRawResponse(client.nav_items)
        self.videos = videos.VideosResourceWithRawResponse(client.videos)
        self.highlander_tournaments = highlander_tournaments.HighlanderTournamentsResourceWithRawResponse(
            client.highlander_tournaments
        )
        self.leagues = leagues.LeaguesResourceWithRawResponse(client.leagues)
        self.schedule_items = schedule_items.ScheduleItemsResourceWithRawResponse(client.schedule_items)
        self.teams = teams.TeamsResourceWithRawResponse(client.teams)
        self.players = players.PlayersResourceWithRawResponse(client.players)


class AsyncLolesportsAPIWithRawResponse:
    def __init__(self, client: AsyncLolesportsAPI) -> None:
        self.get_leagues = get_leagues.AsyncGetLeaguesResourceWithRawResponse(client.get_leagues)
        self.get_schedule = get_schedule.AsyncGetScheduleResourceWithRawResponse(client.get_schedule)
        self.get_live = get_live.AsyncGetLiveResourceWithRawResponse(client.get_live)
        self.get_tournaments_for_league = (
            get_tournaments_for_league.AsyncGetTournamentsForLeagueResourceWithRawResponse(
                client.get_tournaments_for_league
            )
        )
        self.get_standings = get_standings.AsyncGetStandingsResourceWithRawResponse(client.get_standings)
        self.get_completed_events = get_completed_events.AsyncGetCompletedEventsResourceWithRawResponse(
            client.get_completed_events
        )
        self.get_event_details = get_event_details.AsyncGetEventDetailsResourceWithRawResponse(client.get_event_details)
        self.get_teams = get_teams.AsyncGetTeamsResourceWithRawResponse(client.get_teams)
        self.get_games = get_games.AsyncGetGamesResourceWithRawResponse(client.get_games)
        self.window = window.AsyncWindowResourceWithRawResponse(client.window)
        self.details = details.AsyncDetailsResourceWithRawResponse(client.details)
        self.nav_items = nav_items.AsyncNavItemsResourceWithRawResponse(client.nav_items)
        self.videos = videos.AsyncVideosResourceWithRawResponse(client.videos)
        self.highlander_tournaments = highlander_tournaments.AsyncHighlanderTournamentsResourceWithRawResponse(
            client.highlander_tournaments
        )
        self.leagues = leagues.AsyncLeaguesResourceWithRawResponse(client.leagues)
        self.schedule_items = schedule_items.AsyncScheduleItemsResourceWithRawResponse(client.schedule_items)
        self.teams = teams.AsyncTeamsResourceWithRawResponse(client.teams)
        self.players = players.AsyncPlayersResourceWithRawResponse(client.players)


class LolesportsAPIWithStreamedResponse:
    def __init__(self, client: LolesportsAPI) -> None:
        self.get_leagues = get_leagues.GetLeaguesResourceWithStreamingResponse(client.get_leagues)
        self.get_schedule = get_schedule.GetScheduleResourceWithStreamingResponse(client.get_schedule)
        self.get_live = get_live.GetLiveResourceWithStreamingResponse(client.get_live)
        self.get_tournaments_for_league = (
            get_tournaments_for_league.GetTournamentsForLeagueResourceWithStreamingResponse(
                client.get_tournaments_for_league
            )
        )
        self.get_standings = get_standings.GetStandingsResourceWithStreamingResponse(client.get_standings)
        self.get_completed_events = get_completed_events.GetCompletedEventsResourceWithStreamingResponse(
            client.get_completed_events
        )
        self.get_event_details = get_event_details.GetEventDetailsResourceWithStreamingResponse(
            client.get_event_details
        )
        self.get_teams = get_teams.GetTeamsResourceWithStreamingResponse(client.get_teams)
        self.get_games = get_games.GetGamesResourceWithStreamingResponse(client.get_games)
        self.window = window.WindowResourceWithStreamingResponse(client.window)
        self.details = details.DetailsResourceWithStreamingResponse(client.details)
        self.nav_items = nav_items.NavItemsResourceWithStreamingResponse(client.nav_items)
        self.videos = videos.VideosResourceWithStreamingResponse(client.videos)
        self.highlander_tournaments = highlander_tournaments.HighlanderTournamentsResourceWithStreamingResponse(
            client.highlander_tournaments
        )
        self.leagues = leagues.LeaguesResourceWithStreamingResponse(client.leagues)
        self.schedule_items = schedule_items.ScheduleItemsResourceWithStreamingResponse(client.schedule_items)
        self.teams = teams.TeamsResourceWithStreamingResponse(client.teams)
        self.players = players.PlayersResourceWithStreamingResponse(client.players)


class AsyncLolesportsAPIWithStreamedResponse:
    def __init__(self, client: AsyncLolesportsAPI) -> None:
        self.get_leagues = get_leagues.AsyncGetLeaguesResourceWithStreamingResponse(client.get_leagues)
        self.get_schedule = get_schedule.AsyncGetScheduleResourceWithStreamingResponse(client.get_schedule)
        self.get_live = get_live.AsyncGetLiveResourceWithStreamingResponse(client.get_live)
        self.get_tournaments_for_league = (
            get_tournaments_for_league.AsyncGetTournamentsForLeagueResourceWithStreamingResponse(
                client.get_tournaments_for_league
            )
        )
        self.get_standings = get_standings.AsyncGetStandingsResourceWithStreamingResponse(client.get_standings)
        self.get_completed_events = get_completed_events.AsyncGetCompletedEventsResourceWithStreamingResponse(
            client.get_completed_events
        )
        self.get_event_details = get_event_details.AsyncGetEventDetailsResourceWithStreamingResponse(
            client.get_event_details
        )
        self.get_teams = get_teams.AsyncGetTeamsResourceWithStreamingResponse(client.get_teams)
        self.get_games = get_games.AsyncGetGamesResourceWithStreamingResponse(client.get_games)
        self.window = window.AsyncWindowResourceWithStreamingResponse(client.window)
        self.details = details.AsyncDetailsResourceWithStreamingResponse(client.details)
        self.nav_items = nav_items.AsyncNavItemsResourceWithStreamingResponse(client.nav_items)
        self.videos = videos.AsyncVideosResourceWithStreamingResponse(client.videos)
        self.highlander_tournaments = highlander_tournaments.AsyncHighlanderTournamentsResourceWithStreamingResponse(
            client.highlander_tournaments
        )
        self.leagues = leagues.AsyncLeaguesResourceWithStreamingResponse(client.leagues)
        self.schedule_items = schedule_items.AsyncScheduleItemsResourceWithStreamingResponse(client.schedule_items)
        self.teams = teams.AsyncTeamsResourceWithStreamingResponse(client.teams)
        self.players = players.AsyncPlayersResourceWithStreamingResponse(client.players)


Client = LolesportsAPI

AsyncClient = AsyncLolesportsAPI
