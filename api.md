# GetLeagues

Types:

```python
from lolesports_api.types import ExtendedLeague, GetLeagueListResponse
```

Methods:

- <code title="get /getLeagues">client.get_leagues.<a href="./src/lolesports_api/resources/get_leagues.py">list</a>(\*\*<a href="src/lolesports_api/types/get_league_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_league_list_response.py">GetLeagueListResponse</a></code>

# GetSchedule

Types:

```python
from lolesports_api.types import (
    BaseLeague,
    ExtendedEvent,
    Outcome,
    Record,
    GetScheduleRetrieveResponse,
)
```

Methods:

- <code title="get /getSchedule">client.get_schedule.<a href="./src/lolesports_api/resources/get_schedule.py">retrieve</a>(\*\*<a href="src/lolesports_api/types/get_schedule_retrieve_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_schedule_retrieve_response.py">GetScheduleRetrieveResponse</a></code>

# GetLive

Types:

```python
from lolesports_api.types import GetLiveRetrieveResponse
```

Methods:

- <code title="get /getLive">client.get_live.<a href="./src/lolesports_api/resources/get_live.py">retrieve</a>(\*\*<a href="src/lolesports_api/types/get_live_retrieve_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_live_retrieve_response.py">GetLiveRetrieveResponse</a></code>

# GetTournamentsForLeague

Types:

```python
from lolesports_api.types import GetTournamentsForLeagueListResponse
```

Methods:

- <code title="get /getTournamentsForLeague">client.get_tournaments_for_league.<a href="./src/lolesports_api/resources/get_tournaments_for_league.py">list</a>(\*\*<a href="src/lolesports_api/types/get_tournaments_for_league_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_tournaments_for_league_list_response.py">GetTournamentsForLeagueListResponse</a></code>

# GetStandings

Types:

```python
from lolesports_api.types import GetStandingRetrieveResponse
```

Methods:

- <code title="get /getStandings">client.get_standings.<a href="./src/lolesports_api/resources/get_standings.py">retrieve</a>(\*\*<a href="src/lolesports_api/types/get_standing_retrieve_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_standing_retrieve_response.py">GetStandingRetrieveResponse</a></code>

# GetCompletedEvents

Types:

```python
from lolesports_api.types import SimpleEvent, SimpleMatch, GetCompletedEventListResponse
```

Methods:

- <code title="get /getCompletedEvents">client.get_completed_events.<a href="./src/lolesports_api/resources/get_completed_events.py">list</a>(\*\*<a href="src/lolesports_api/types/get_completed_event_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_completed_event_list_response.py">GetCompletedEventListResponse</a></code>

# GetEventDetails

Types:

```python
from lolesports_api.types import (
    BaseMatch,
    BaseStrategy,
    EventType,
    ExtendedVod,
    Result,
    SimpleLeague,
    Vod,
    GetEventDetailRetrieveResponse,
)
```

Methods:

- <code title="get /getEventDetails">client.get_event_details.<a href="./src/lolesports_api/resources/get_event_details.py">retrieve</a>(\*\*<a href="src/lolesports_api/types/get_event_detail_retrieve_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_event_detail_retrieve_response.py">GetEventDetailRetrieveResponse</a></code>

# GetTeams

Types:

```python
from lolesports_api.types import Team, GetTeamListResponse
```

Methods:

- <code title="get /getTeams">client.get_teams.<a href="./src/lolesports_api/resources/get_teams.py">list</a>(\*\*<a href="src/lolesports_api/types/get_team_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_team_list_response.py">GetTeamListResponse</a></code>

# GetGames

Types:

```python
from lolesports_api.types import SimpleGame, State, GetGameListResponse
```

Methods:

- <code title="get /getGames">client.get_games.<a href="./src/lolesports_api/resources/get_games.py">list</a>(\*\*<a href="src/lolesports_api/types/get_game_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/get_game_list_response.py">GetGameListResponse</a></code>

# Window

Types:

```python
from lolesports_api.types import (
    ParticipantMetadata,
    TeamMetadata,
    TeamStats,
    WindowRetrieveResponse,
)
```

Methods:

- <code title="get /window/{gameId}">client.window.<a href="./src/lolesports_api/resources/window.py">retrieve</a>(game_id, \*\*<a href="src/lolesports_api/types/window_retrieve_params.py">params</a>) -> <a href="./src/lolesports_api/types/window_retrieve_response.py">WindowRetrieveResponse</a></code>

# Details

Types:

```python
from lolesports_api.types import BaseFrame, ParticipantID, ParticipantStats, DetailRetrieveResponse
```

Methods:

- <code title="get /details/{gameId}">client.details.<a href="./src/lolesports_api/resources/details.py">retrieve</a>(game_id, \*\*<a href="src/lolesports_api/types/detail_retrieve_params.py">params</a>) -> <a href="./src/lolesports_api/types/detail_retrieve_response.py">DetailRetrieveResponse</a></code>

# NavItems

Types:

```python
from lolesports_api.types import HighlanderLeague, NavItem, NavItemListResponse
```

Methods:

- <code title="get /navItems">client.nav_items.<a href="./src/lolesports_api/resources/nav_items.py">list</a>() -> <a href="./src/lolesports_api/types/nav_item_list_response.py">NavItemListResponse</a></code>

# Videos

Types:

```python
from lolesports_api.types import VideoListResponse
```

Methods:

- <code title="get /videos">client.videos.<a href="./src/lolesports_api/resources/videos.py">list</a>() -> <a href="./src/lolesports_api/types/video_list_response.py">VideoListResponse</a></code>

# HighlanderTournaments

Types:

```python
from lolesports_api.types import (
    HighlanderTournament,
    Role,
    RosteringStrategy,
    Standings,
    HighlanderTournamentListResponse,
)
```

Methods:

- <code title="get /highlanderTournaments">client.highlander_tournaments.<a href="./src/lolesports_api/resources/highlander_tournaments.py">list</a>(\*\*<a href="src/lolesports_api/types/highlander_tournament_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/highlander_tournament_list_response.py">HighlanderTournamentListResponse</a></code>

# Leagues

Types:

```python
from lolesports_api.types import HighlanderPlayer, HighlanderRecord, LeagueListResponse
```

Methods:

- <code title="get /leagues">client.leagues.<a href="./src/lolesports_api/resources/leagues.py">list</a>(\*\*<a href="src/lolesports_api/types/league_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/league_list_response.py">LeagueListResponse</a></code>

# ScheduleItems

Types:

```python
from lolesports_api.types import ScheduleItem, ScheduleItemListResponse
```

Methods:

- <code title="get /scheduleItems">client.schedule_items.<a href="./src/lolesports_api/resources/schedule_items.py">list</a>(\*\*<a href="src/lolesports_api/types/schedule_item_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/schedule_item_list_response.py">ScheduleItemListResponse</a></code>

# Teams

Types:

```python
from lolesports_api.types import TeamListResponse
```

Methods:

- <code title="get /teams">client.teams.<a href="./src/lolesports_api/resources/teams.py">list</a>(\*\*<a href="src/lolesports_api/types/team_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/team_list_response.py">TeamListResponse</a></code>

# Players

Types:

```python
from lolesports_api.types import (
    BaseScheduleItem,
    ForeignIDs,
    HighlanderTeam,
    MatchScheduleItem,
    PlayerListResponse,
)
```

Methods:

- <code title="get /players">client.players.<a href="./src/lolesports_api/resources/players.py">list</a>(\*\*<a href="src/lolesports_api/types/player_list_params.py">params</a>) -> <a href="./src/lolesports_api/types/player_list_response.py">PlayerListResponse</a></code>
