# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, LolesportsAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
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
    from .resources.teams import TeamsResource, AsyncTeamsResource
    from .resources.videos import VideosResource, AsyncVideosResource
    from .resources.window import WindowResource, AsyncWindowResource
    from .resources.details import DetailsResource, AsyncDetailsResource
    from .resources.leagues import LeaguesResource, AsyncLeaguesResource
    from .resources.players import PlayersResource, AsyncPlayersResource
    from .resources.get_live import GetLiveResource, AsyncGetLiveResource
    from .resources.get_games import GetGamesResource, AsyncGetGamesResource
    from .resources.get_teams import GetTeamsResource, AsyncGetTeamsResource
    from .resources.nav_items import NavItemsResource, AsyncNavItemsResource
    from .resources.get_leagues import GetLeaguesResource, AsyncGetLeaguesResource
    from .resources.get_schedule import GetScheduleResource, AsyncGetScheduleResource
    from .resources.get_standings import GetStandingsResource, AsyncGetStandingsResource
    from .resources.schedule_items import ScheduleItemsResource, AsyncScheduleItemsResource
    from .resources.get_event_details import GetEventDetailsResource, AsyncGetEventDetailsResource
    from .resources.get_completed_events import GetCompletedEventsResource, AsyncGetCompletedEventsResource
    from .resources.highlander_tournaments import HighlanderTournamentsResource, AsyncHighlanderTournamentsResource
    from .resources.get_tournaments_for_league import (
        GetTournamentsForLeagueResource,
        AsyncGetTournamentsForLeagueResource,
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

    @cached_property
    def get_leagues(self) -> GetLeaguesResource:
        from .resources.get_leagues import GetLeaguesResource

        return GetLeaguesResource(self)

    @cached_property
    def get_schedule(self) -> GetScheduleResource:
        from .resources.get_schedule import GetScheduleResource

        return GetScheduleResource(self)

    @cached_property
    def get_live(self) -> GetLiveResource:
        from .resources.get_live import GetLiveResource

        return GetLiveResource(self)

    @cached_property
    def get_tournaments_for_league(self) -> GetTournamentsForLeagueResource:
        from .resources.get_tournaments_for_league import GetTournamentsForLeagueResource

        return GetTournamentsForLeagueResource(self)

    @cached_property
    def get_standings(self) -> GetStandingsResource:
        from .resources.get_standings import GetStandingsResource

        return GetStandingsResource(self)

    @cached_property
    def get_completed_events(self) -> GetCompletedEventsResource:
        from .resources.get_completed_events import GetCompletedEventsResource

        return GetCompletedEventsResource(self)

    @cached_property
    def get_event_details(self) -> GetEventDetailsResource:
        from .resources.get_event_details import GetEventDetailsResource

        return GetEventDetailsResource(self)

    @cached_property
    def get_teams(self) -> GetTeamsResource:
        from .resources.get_teams import GetTeamsResource

        return GetTeamsResource(self)

    @cached_property
    def get_games(self) -> GetGamesResource:
        from .resources.get_games import GetGamesResource

        return GetGamesResource(self)

    @cached_property
    def window(self) -> WindowResource:
        from .resources.window import WindowResource

        return WindowResource(self)

    @cached_property
    def details(self) -> DetailsResource:
        from .resources.details import DetailsResource

        return DetailsResource(self)

    @cached_property
    def nav_items(self) -> NavItemsResource:
        from .resources.nav_items import NavItemsResource

        return NavItemsResource(self)

    @cached_property
    def videos(self) -> VideosResource:
        from .resources.videos import VideosResource

        return VideosResource(self)

    @cached_property
    def highlander_tournaments(self) -> HighlanderTournamentsResource:
        from .resources.highlander_tournaments import HighlanderTournamentsResource

        return HighlanderTournamentsResource(self)

    @cached_property
    def leagues(self) -> LeaguesResource:
        from .resources.leagues import LeaguesResource

        return LeaguesResource(self)

    @cached_property
    def schedule_items(self) -> ScheduleItemsResource:
        from .resources.schedule_items import ScheduleItemsResource

        return ScheduleItemsResource(self)

    @cached_property
    def teams(self) -> TeamsResource:
        from .resources.teams import TeamsResource

        return TeamsResource(self)

    @cached_property
    def players(self) -> PlayersResource:
        from .resources.players import PlayersResource

        return PlayersResource(self)

    @cached_property
    def with_raw_response(self) -> LolesportsAPIWithRawResponse:
        return LolesportsAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LolesportsAPIWithStreamedResponse:
        return LolesportsAPIWithStreamedResponse(self)

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

    @cached_property
    def get_leagues(self) -> AsyncGetLeaguesResource:
        from .resources.get_leagues import AsyncGetLeaguesResource

        return AsyncGetLeaguesResource(self)

    @cached_property
    def get_schedule(self) -> AsyncGetScheduleResource:
        from .resources.get_schedule import AsyncGetScheduleResource

        return AsyncGetScheduleResource(self)

    @cached_property
    def get_live(self) -> AsyncGetLiveResource:
        from .resources.get_live import AsyncGetLiveResource

        return AsyncGetLiveResource(self)

    @cached_property
    def get_tournaments_for_league(self) -> AsyncGetTournamentsForLeagueResource:
        from .resources.get_tournaments_for_league import AsyncGetTournamentsForLeagueResource

        return AsyncGetTournamentsForLeagueResource(self)

    @cached_property
    def get_standings(self) -> AsyncGetStandingsResource:
        from .resources.get_standings import AsyncGetStandingsResource

        return AsyncGetStandingsResource(self)

    @cached_property
    def get_completed_events(self) -> AsyncGetCompletedEventsResource:
        from .resources.get_completed_events import AsyncGetCompletedEventsResource

        return AsyncGetCompletedEventsResource(self)

    @cached_property
    def get_event_details(self) -> AsyncGetEventDetailsResource:
        from .resources.get_event_details import AsyncGetEventDetailsResource

        return AsyncGetEventDetailsResource(self)

    @cached_property
    def get_teams(self) -> AsyncGetTeamsResource:
        from .resources.get_teams import AsyncGetTeamsResource

        return AsyncGetTeamsResource(self)

    @cached_property
    def get_games(self) -> AsyncGetGamesResource:
        from .resources.get_games import AsyncGetGamesResource

        return AsyncGetGamesResource(self)

    @cached_property
    def window(self) -> AsyncWindowResource:
        from .resources.window import AsyncWindowResource

        return AsyncWindowResource(self)

    @cached_property
    def details(self) -> AsyncDetailsResource:
        from .resources.details import AsyncDetailsResource

        return AsyncDetailsResource(self)

    @cached_property
    def nav_items(self) -> AsyncNavItemsResource:
        from .resources.nav_items import AsyncNavItemsResource

        return AsyncNavItemsResource(self)

    @cached_property
    def videos(self) -> AsyncVideosResource:
        from .resources.videos import AsyncVideosResource

        return AsyncVideosResource(self)

    @cached_property
    def highlander_tournaments(self) -> AsyncHighlanderTournamentsResource:
        from .resources.highlander_tournaments import AsyncHighlanderTournamentsResource

        return AsyncHighlanderTournamentsResource(self)

    @cached_property
    def leagues(self) -> AsyncLeaguesResource:
        from .resources.leagues import AsyncLeaguesResource

        return AsyncLeaguesResource(self)

    @cached_property
    def schedule_items(self) -> AsyncScheduleItemsResource:
        from .resources.schedule_items import AsyncScheduleItemsResource

        return AsyncScheduleItemsResource(self)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        from .resources.teams import AsyncTeamsResource

        return AsyncTeamsResource(self)

    @cached_property
    def players(self) -> AsyncPlayersResource:
        from .resources.players import AsyncPlayersResource

        return AsyncPlayersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLolesportsAPIWithRawResponse:
        return AsyncLolesportsAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLolesportsAPIWithStreamedResponse:
        return AsyncLolesportsAPIWithStreamedResponse(self)

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
    _client: LolesportsAPI

    def __init__(self, client: LolesportsAPI) -> None:
        self._client = client

    @cached_property
    def get_leagues(self) -> get_leagues.GetLeaguesResourceWithRawResponse:
        from .resources.get_leagues import GetLeaguesResourceWithRawResponse

        return GetLeaguesResourceWithRawResponse(self._client.get_leagues)

    @cached_property
    def get_schedule(self) -> get_schedule.GetScheduleResourceWithRawResponse:
        from .resources.get_schedule import GetScheduleResourceWithRawResponse

        return GetScheduleResourceWithRawResponse(self._client.get_schedule)

    @cached_property
    def get_live(self) -> get_live.GetLiveResourceWithRawResponse:
        from .resources.get_live import GetLiveResourceWithRawResponse

        return GetLiveResourceWithRawResponse(self._client.get_live)

    @cached_property
    def get_tournaments_for_league(self) -> get_tournaments_for_league.GetTournamentsForLeagueResourceWithRawResponse:
        from .resources.get_tournaments_for_league import GetTournamentsForLeagueResourceWithRawResponse

        return GetTournamentsForLeagueResourceWithRawResponse(self._client.get_tournaments_for_league)

    @cached_property
    def get_standings(self) -> get_standings.GetStandingsResourceWithRawResponse:
        from .resources.get_standings import GetStandingsResourceWithRawResponse

        return GetStandingsResourceWithRawResponse(self._client.get_standings)

    @cached_property
    def get_completed_events(self) -> get_completed_events.GetCompletedEventsResourceWithRawResponse:
        from .resources.get_completed_events import GetCompletedEventsResourceWithRawResponse

        return GetCompletedEventsResourceWithRawResponse(self._client.get_completed_events)

    @cached_property
    def get_event_details(self) -> get_event_details.GetEventDetailsResourceWithRawResponse:
        from .resources.get_event_details import GetEventDetailsResourceWithRawResponse

        return GetEventDetailsResourceWithRawResponse(self._client.get_event_details)

    @cached_property
    def get_teams(self) -> get_teams.GetTeamsResourceWithRawResponse:
        from .resources.get_teams import GetTeamsResourceWithRawResponse

        return GetTeamsResourceWithRawResponse(self._client.get_teams)

    @cached_property
    def get_games(self) -> get_games.GetGamesResourceWithRawResponse:
        from .resources.get_games import GetGamesResourceWithRawResponse

        return GetGamesResourceWithRawResponse(self._client.get_games)

    @cached_property
    def window(self) -> window.WindowResourceWithRawResponse:
        from .resources.window import WindowResourceWithRawResponse

        return WindowResourceWithRawResponse(self._client.window)

    @cached_property
    def details(self) -> details.DetailsResourceWithRawResponse:
        from .resources.details import DetailsResourceWithRawResponse

        return DetailsResourceWithRawResponse(self._client.details)

    @cached_property
    def nav_items(self) -> nav_items.NavItemsResourceWithRawResponse:
        from .resources.nav_items import NavItemsResourceWithRawResponse

        return NavItemsResourceWithRawResponse(self._client.nav_items)

    @cached_property
    def videos(self) -> videos.VideosResourceWithRawResponse:
        from .resources.videos import VideosResourceWithRawResponse

        return VideosResourceWithRawResponse(self._client.videos)

    @cached_property
    def highlander_tournaments(self) -> highlander_tournaments.HighlanderTournamentsResourceWithRawResponse:
        from .resources.highlander_tournaments import HighlanderTournamentsResourceWithRawResponse

        return HighlanderTournamentsResourceWithRawResponse(self._client.highlander_tournaments)

    @cached_property
    def leagues(self) -> leagues.LeaguesResourceWithRawResponse:
        from .resources.leagues import LeaguesResourceWithRawResponse

        return LeaguesResourceWithRawResponse(self._client.leagues)

    @cached_property
    def schedule_items(self) -> schedule_items.ScheduleItemsResourceWithRawResponse:
        from .resources.schedule_items import ScheduleItemsResourceWithRawResponse

        return ScheduleItemsResourceWithRawResponse(self._client.schedule_items)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithRawResponse:
        from .resources.teams import TeamsResourceWithRawResponse

        return TeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def players(self) -> players.PlayersResourceWithRawResponse:
        from .resources.players import PlayersResourceWithRawResponse

        return PlayersResourceWithRawResponse(self._client.players)


class AsyncLolesportsAPIWithRawResponse:
    _client: AsyncLolesportsAPI

    def __init__(self, client: AsyncLolesportsAPI) -> None:
        self._client = client

    @cached_property
    def get_leagues(self) -> get_leagues.AsyncGetLeaguesResourceWithRawResponse:
        from .resources.get_leagues import AsyncGetLeaguesResourceWithRawResponse

        return AsyncGetLeaguesResourceWithRawResponse(self._client.get_leagues)

    @cached_property
    def get_schedule(self) -> get_schedule.AsyncGetScheduleResourceWithRawResponse:
        from .resources.get_schedule import AsyncGetScheduleResourceWithRawResponse

        return AsyncGetScheduleResourceWithRawResponse(self._client.get_schedule)

    @cached_property
    def get_live(self) -> get_live.AsyncGetLiveResourceWithRawResponse:
        from .resources.get_live import AsyncGetLiveResourceWithRawResponse

        return AsyncGetLiveResourceWithRawResponse(self._client.get_live)

    @cached_property
    def get_tournaments_for_league(
        self,
    ) -> get_tournaments_for_league.AsyncGetTournamentsForLeagueResourceWithRawResponse:
        from .resources.get_tournaments_for_league import AsyncGetTournamentsForLeagueResourceWithRawResponse

        return AsyncGetTournamentsForLeagueResourceWithRawResponse(self._client.get_tournaments_for_league)

    @cached_property
    def get_standings(self) -> get_standings.AsyncGetStandingsResourceWithRawResponse:
        from .resources.get_standings import AsyncGetStandingsResourceWithRawResponse

        return AsyncGetStandingsResourceWithRawResponse(self._client.get_standings)

    @cached_property
    def get_completed_events(self) -> get_completed_events.AsyncGetCompletedEventsResourceWithRawResponse:
        from .resources.get_completed_events import AsyncGetCompletedEventsResourceWithRawResponse

        return AsyncGetCompletedEventsResourceWithRawResponse(self._client.get_completed_events)

    @cached_property
    def get_event_details(self) -> get_event_details.AsyncGetEventDetailsResourceWithRawResponse:
        from .resources.get_event_details import AsyncGetEventDetailsResourceWithRawResponse

        return AsyncGetEventDetailsResourceWithRawResponse(self._client.get_event_details)

    @cached_property
    def get_teams(self) -> get_teams.AsyncGetTeamsResourceWithRawResponse:
        from .resources.get_teams import AsyncGetTeamsResourceWithRawResponse

        return AsyncGetTeamsResourceWithRawResponse(self._client.get_teams)

    @cached_property
    def get_games(self) -> get_games.AsyncGetGamesResourceWithRawResponse:
        from .resources.get_games import AsyncGetGamesResourceWithRawResponse

        return AsyncGetGamesResourceWithRawResponse(self._client.get_games)

    @cached_property
    def window(self) -> window.AsyncWindowResourceWithRawResponse:
        from .resources.window import AsyncWindowResourceWithRawResponse

        return AsyncWindowResourceWithRawResponse(self._client.window)

    @cached_property
    def details(self) -> details.AsyncDetailsResourceWithRawResponse:
        from .resources.details import AsyncDetailsResourceWithRawResponse

        return AsyncDetailsResourceWithRawResponse(self._client.details)

    @cached_property
    def nav_items(self) -> nav_items.AsyncNavItemsResourceWithRawResponse:
        from .resources.nav_items import AsyncNavItemsResourceWithRawResponse

        return AsyncNavItemsResourceWithRawResponse(self._client.nav_items)

    @cached_property
    def videos(self) -> videos.AsyncVideosResourceWithRawResponse:
        from .resources.videos import AsyncVideosResourceWithRawResponse

        return AsyncVideosResourceWithRawResponse(self._client.videos)

    @cached_property
    def highlander_tournaments(self) -> highlander_tournaments.AsyncHighlanderTournamentsResourceWithRawResponse:
        from .resources.highlander_tournaments import AsyncHighlanderTournamentsResourceWithRawResponse

        return AsyncHighlanderTournamentsResourceWithRawResponse(self._client.highlander_tournaments)

    @cached_property
    def leagues(self) -> leagues.AsyncLeaguesResourceWithRawResponse:
        from .resources.leagues import AsyncLeaguesResourceWithRawResponse

        return AsyncLeaguesResourceWithRawResponse(self._client.leagues)

    @cached_property
    def schedule_items(self) -> schedule_items.AsyncScheduleItemsResourceWithRawResponse:
        from .resources.schedule_items import AsyncScheduleItemsResourceWithRawResponse

        return AsyncScheduleItemsResourceWithRawResponse(self._client.schedule_items)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithRawResponse:
        from .resources.teams import AsyncTeamsResourceWithRawResponse

        return AsyncTeamsResourceWithRawResponse(self._client.teams)

    @cached_property
    def players(self) -> players.AsyncPlayersResourceWithRawResponse:
        from .resources.players import AsyncPlayersResourceWithRawResponse

        return AsyncPlayersResourceWithRawResponse(self._client.players)


class LolesportsAPIWithStreamedResponse:
    _client: LolesportsAPI

    def __init__(self, client: LolesportsAPI) -> None:
        self._client = client

    @cached_property
    def get_leagues(self) -> get_leagues.GetLeaguesResourceWithStreamingResponse:
        from .resources.get_leagues import GetLeaguesResourceWithStreamingResponse

        return GetLeaguesResourceWithStreamingResponse(self._client.get_leagues)

    @cached_property
    def get_schedule(self) -> get_schedule.GetScheduleResourceWithStreamingResponse:
        from .resources.get_schedule import GetScheduleResourceWithStreamingResponse

        return GetScheduleResourceWithStreamingResponse(self._client.get_schedule)

    @cached_property
    def get_live(self) -> get_live.GetLiveResourceWithStreamingResponse:
        from .resources.get_live import GetLiveResourceWithStreamingResponse

        return GetLiveResourceWithStreamingResponse(self._client.get_live)

    @cached_property
    def get_tournaments_for_league(
        self,
    ) -> get_tournaments_for_league.GetTournamentsForLeagueResourceWithStreamingResponse:
        from .resources.get_tournaments_for_league import GetTournamentsForLeagueResourceWithStreamingResponse

        return GetTournamentsForLeagueResourceWithStreamingResponse(self._client.get_tournaments_for_league)

    @cached_property
    def get_standings(self) -> get_standings.GetStandingsResourceWithStreamingResponse:
        from .resources.get_standings import GetStandingsResourceWithStreamingResponse

        return GetStandingsResourceWithStreamingResponse(self._client.get_standings)

    @cached_property
    def get_completed_events(self) -> get_completed_events.GetCompletedEventsResourceWithStreamingResponse:
        from .resources.get_completed_events import GetCompletedEventsResourceWithStreamingResponse

        return GetCompletedEventsResourceWithStreamingResponse(self._client.get_completed_events)

    @cached_property
    def get_event_details(self) -> get_event_details.GetEventDetailsResourceWithStreamingResponse:
        from .resources.get_event_details import GetEventDetailsResourceWithStreamingResponse

        return GetEventDetailsResourceWithStreamingResponse(self._client.get_event_details)

    @cached_property
    def get_teams(self) -> get_teams.GetTeamsResourceWithStreamingResponse:
        from .resources.get_teams import GetTeamsResourceWithStreamingResponse

        return GetTeamsResourceWithStreamingResponse(self._client.get_teams)

    @cached_property
    def get_games(self) -> get_games.GetGamesResourceWithStreamingResponse:
        from .resources.get_games import GetGamesResourceWithStreamingResponse

        return GetGamesResourceWithStreamingResponse(self._client.get_games)

    @cached_property
    def window(self) -> window.WindowResourceWithStreamingResponse:
        from .resources.window import WindowResourceWithStreamingResponse

        return WindowResourceWithStreamingResponse(self._client.window)

    @cached_property
    def details(self) -> details.DetailsResourceWithStreamingResponse:
        from .resources.details import DetailsResourceWithStreamingResponse

        return DetailsResourceWithStreamingResponse(self._client.details)

    @cached_property
    def nav_items(self) -> nav_items.NavItemsResourceWithStreamingResponse:
        from .resources.nav_items import NavItemsResourceWithStreamingResponse

        return NavItemsResourceWithStreamingResponse(self._client.nav_items)

    @cached_property
    def videos(self) -> videos.VideosResourceWithStreamingResponse:
        from .resources.videos import VideosResourceWithStreamingResponse

        return VideosResourceWithStreamingResponse(self._client.videos)

    @cached_property
    def highlander_tournaments(self) -> highlander_tournaments.HighlanderTournamentsResourceWithStreamingResponse:
        from .resources.highlander_tournaments import HighlanderTournamentsResourceWithStreamingResponse

        return HighlanderTournamentsResourceWithStreamingResponse(self._client.highlander_tournaments)

    @cached_property
    def leagues(self) -> leagues.LeaguesResourceWithStreamingResponse:
        from .resources.leagues import LeaguesResourceWithStreamingResponse

        return LeaguesResourceWithStreamingResponse(self._client.leagues)

    @cached_property
    def schedule_items(self) -> schedule_items.ScheduleItemsResourceWithStreamingResponse:
        from .resources.schedule_items import ScheduleItemsResourceWithStreamingResponse

        return ScheduleItemsResourceWithStreamingResponse(self._client.schedule_items)

    @cached_property
    def teams(self) -> teams.TeamsResourceWithStreamingResponse:
        from .resources.teams import TeamsResourceWithStreamingResponse

        return TeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def players(self) -> players.PlayersResourceWithStreamingResponse:
        from .resources.players import PlayersResourceWithStreamingResponse

        return PlayersResourceWithStreamingResponse(self._client.players)


class AsyncLolesportsAPIWithStreamedResponse:
    _client: AsyncLolesportsAPI

    def __init__(self, client: AsyncLolesportsAPI) -> None:
        self._client = client

    @cached_property
    def get_leagues(self) -> get_leagues.AsyncGetLeaguesResourceWithStreamingResponse:
        from .resources.get_leagues import AsyncGetLeaguesResourceWithStreamingResponse

        return AsyncGetLeaguesResourceWithStreamingResponse(self._client.get_leagues)

    @cached_property
    def get_schedule(self) -> get_schedule.AsyncGetScheduleResourceWithStreamingResponse:
        from .resources.get_schedule import AsyncGetScheduleResourceWithStreamingResponse

        return AsyncGetScheduleResourceWithStreamingResponse(self._client.get_schedule)

    @cached_property
    def get_live(self) -> get_live.AsyncGetLiveResourceWithStreamingResponse:
        from .resources.get_live import AsyncGetLiveResourceWithStreamingResponse

        return AsyncGetLiveResourceWithStreamingResponse(self._client.get_live)

    @cached_property
    def get_tournaments_for_league(
        self,
    ) -> get_tournaments_for_league.AsyncGetTournamentsForLeagueResourceWithStreamingResponse:
        from .resources.get_tournaments_for_league import AsyncGetTournamentsForLeagueResourceWithStreamingResponse

        return AsyncGetTournamentsForLeagueResourceWithStreamingResponse(self._client.get_tournaments_for_league)

    @cached_property
    def get_standings(self) -> get_standings.AsyncGetStandingsResourceWithStreamingResponse:
        from .resources.get_standings import AsyncGetStandingsResourceWithStreamingResponse

        return AsyncGetStandingsResourceWithStreamingResponse(self._client.get_standings)

    @cached_property
    def get_completed_events(self) -> get_completed_events.AsyncGetCompletedEventsResourceWithStreamingResponse:
        from .resources.get_completed_events import AsyncGetCompletedEventsResourceWithStreamingResponse

        return AsyncGetCompletedEventsResourceWithStreamingResponse(self._client.get_completed_events)

    @cached_property
    def get_event_details(self) -> get_event_details.AsyncGetEventDetailsResourceWithStreamingResponse:
        from .resources.get_event_details import AsyncGetEventDetailsResourceWithStreamingResponse

        return AsyncGetEventDetailsResourceWithStreamingResponse(self._client.get_event_details)

    @cached_property
    def get_teams(self) -> get_teams.AsyncGetTeamsResourceWithStreamingResponse:
        from .resources.get_teams import AsyncGetTeamsResourceWithStreamingResponse

        return AsyncGetTeamsResourceWithStreamingResponse(self._client.get_teams)

    @cached_property
    def get_games(self) -> get_games.AsyncGetGamesResourceWithStreamingResponse:
        from .resources.get_games import AsyncGetGamesResourceWithStreamingResponse

        return AsyncGetGamesResourceWithStreamingResponse(self._client.get_games)

    @cached_property
    def window(self) -> window.AsyncWindowResourceWithStreamingResponse:
        from .resources.window import AsyncWindowResourceWithStreamingResponse

        return AsyncWindowResourceWithStreamingResponse(self._client.window)

    @cached_property
    def details(self) -> details.AsyncDetailsResourceWithStreamingResponse:
        from .resources.details import AsyncDetailsResourceWithStreamingResponse

        return AsyncDetailsResourceWithStreamingResponse(self._client.details)

    @cached_property
    def nav_items(self) -> nav_items.AsyncNavItemsResourceWithStreamingResponse:
        from .resources.nav_items import AsyncNavItemsResourceWithStreamingResponse

        return AsyncNavItemsResourceWithStreamingResponse(self._client.nav_items)

    @cached_property
    def videos(self) -> videos.AsyncVideosResourceWithStreamingResponse:
        from .resources.videos import AsyncVideosResourceWithStreamingResponse

        return AsyncVideosResourceWithStreamingResponse(self._client.videos)

    @cached_property
    def highlander_tournaments(self) -> highlander_tournaments.AsyncHighlanderTournamentsResourceWithStreamingResponse:
        from .resources.highlander_tournaments import AsyncHighlanderTournamentsResourceWithStreamingResponse

        return AsyncHighlanderTournamentsResourceWithStreamingResponse(self._client.highlander_tournaments)

    @cached_property
    def leagues(self) -> leagues.AsyncLeaguesResourceWithStreamingResponse:
        from .resources.leagues import AsyncLeaguesResourceWithStreamingResponse

        return AsyncLeaguesResourceWithStreamingResponse(self._client.leagues)

    @cached_property
    def schedule_items(self) -> schedule_items.AsyncScheduleItemsResourceWithStreamingResponse:
        from .resources.schedule_items import AsyncScheduleItemsResourceWithStreamingResponse

        return AsyncScheduleItemsResourceWithStreamingResponse(self._client.schedule_items)

    @cached_property
    def teams(self) -> teams.AsyncTeamsResourceWithStreamingResponse:
        from .resources.teams import AsyncTeamsResourceWithStreamingResponse

        return AsyncTeamsResourceWithStreamingResponse(self._client.teams)

    @cached_property
    def players(self) -> players.AsyncPlayersResourceWithStreamingResponse:
        from .resources.players import AsyncPlayersResourceWithStreamingResponse

        return AsyncPlayersResourceWithStreamingResponse(self._client.players)


Client = LolesportsAPI

AsyncClient = AsyncLolesportsAPI
