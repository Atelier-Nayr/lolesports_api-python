# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    nav_item,
    standings,
    team_list_response,
    league_list_response,
    player_list_response,
    highlander_tournament,
    nav_item_list_response,
    schedule_item_list_response,
)
from .. import _compat
from .vod import Vod as Vod
from .role import Role as Role
from .team import Team as Team
from .state import State as State
from .record import Record as Record
from .result import Result as Result
from .outcome import Outcome as Outcome
from .nav_item import NavItem as NavItem
from .standings import Standings as Standings
from .base_frame import BaseFrame as BaseFrame
from .base_match import BaseMatch as BaseMatch
from .event_type import EventType as EventType
from .team_stats import TeamStats as TeamStats
from .base_league import BaseLeague as BaseLeague
from .foreign_ids import ForeignIDs as ForeignIDs
from .simple_game import SimpleGame as SimpleGame
from .extended_vod import ExtendedVod as ExtendedVod
from .simple_event import SimpleEvent as SimpleEvent
from .simple_match import SimpleMatch as SimpleMatch
from .base_strategy import BaseStrategy as BaseStrategy
from .schedule_item import ScheduleItem as ScheduleItem
from .simple_league import SimpleLeague as SimpleLeague
from .team_metadata import TeamMetadata as TeamMetadata
from .extended_event import ExtendedEvent as ExtendedEvent
from .participant_id import ParticipantID as ParticipantID
from .extended_league import ExtendedLeague as ExtendedLeague
from .highlander_team import HighlanderTeam as HighlanderTeam
from .team_list_params import TeamListParams as TeamListParams
from .highlander_league import HighlanderLeague as HighlanderLeague
from .highlander_player import HighlanderPlayer as HighlanderPlayer
from .highlander_record import HighlanderRecord as HighlanderRecord
from .participant_stats import ParticipantStats as ParticipantStats
from .base_schedule_item import BaseScheduleItem as BaseScheduleItem
from .league_list_params import LeagueListParams as LeagueListParams
from .player_list_params import PlayerListParams as PlayerListParams
from .rostering_strategy import RosteringStrategy as RosteringStrategy
from .team_list_response import TeamListResponse as TeamListResponse
from .match_schedule_item import MatchScheduleItem as MatchScheduleItem
from .video_list_response import VideoListResponse as VideoListResponse
from .get_game_list_params import GetGameListParams as GetGameListParams
from .get_team_list_params import GetTeamListParams as GetTeamListParams
from .league_list_response import LeagueListResponse as LeagueListResponse
from .participant_metadata import ParticipantMetadata as ParticipantMetadata
from .player_list_response import PlayerListResponse as PlayerListResponse
from .highlander_tournament import HighlanderTournament as HighlanderTournament
from .detail_retrieve_params import DetailRetrieveParams as DetailRetrieveParams
from .get_game_list_response import GetGameListResponse as GetGameListResponse
from .get_league_list_params import GetLeagueListParams as GetLeagueListParams
from .get_team_list_response import GetTeamListResponse as GetTeamListResponse
from .nav_item_list_response import NavItemListResponse as NavItemListResponse
from .window_retrieve_params import WindowRetrieveParams as WindowRetrieveParams
from .detail_retrieve_response import DetailRetrieveResponse as DetailRetrieveResponse
from .get_league_list_response import GetLeagueListResponse as GetLeagueListResponse
from .get_live_retrieve_params import GetLiveRetrieveParams as GetLiveRetrieveParams
from .window_retrieve_response import WindowRetrieveResponse as WindowRetrieveResponse
from .schedule_item_list_params import ScheduleItemListParams as ScheduleItemListParams
from .get_live_retrieve_response import GetLiveRetrieveResponse as GetLiveRetrieveResponse
from .schedule_item_list_response import ScheduleItemListResponse as ScheduleItemListResponse
from .get_schedule_retrieve_params import GetScheduleRetrieveParams as GetScheduleRetrieveParams
from .get_standing_retrieve_params import GetStandingRetrieveParams as GetStandingRetrieveParams
from .get_schedule_retrieve_response import GetScheduleRetrieveResponse as GetScheduleRetrieveResponse
from .get_standing_retrieve_response import GetStandingRetrieveResponse as GetStandingRetrieveResponse
from .get_completed_event_list_params import GetCompletedEventListParams as GetCompletedEventListParams
from .get_event_detail_retrieve_params import GetEventDetailRetrieveParams as GetEventDetailRetrieveParams
from .get_completed_event_list_response import GetCompletedEventListResponse as GetCompletedEventListResponse
from .highlander_tournament_list_params import HighlanderTournamentListParams as HighlanderTournamentListParams
from .get_event_detail_retrieve_response import GetEventDetailRetrieveResponse as GetEventDetailRetrieveResponse
from .highlander_tournament_list_response import HighlanderTournamentListResponse as HighlanderTournamentListResponse
from .get_tournaments_for_league_list_params import (
    GetTournamentsForLeagueListParams as GetTournamentsForLeagueListParams,
)
from .get_tournaments_for_league_list_response import (
    GetTournamentsForLeagueListResponse as GetTournamentsForLeagueListResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    nav_item.NavItem.update_forward_refs()  # type: ignore
    nav_item_list_response.NavItemListResponse.update_forward_refs()  # type: ignore
    highlander_tournament.HighlanderTournament.update_forward_refs()  # type: ignore
    standings.Standings.update_forward_refs()  # type: ignore
    league_list_response.LeagueListResponse.update_forward_refs()  # type: ignore
    schedule_item_list_response.ScheduleItemListResponse.update_forward_refs()  # type: ignore
    team_list_response.TeamListResponse.update_forward_refs()  # type: ignore
    player_list_response.PlayerListResponse.update_forward_refs()  # type: ignore
else:
    nav_item.NavItem.model_rebuild(_parent_namespace_depth=0)
    nav_item_list_response.NavItemListResponse.model_rebuild(_parent_namespace_depth=0)
    highlander_tournament.HighlanderTournament.model_rebuild(_parent_namespace_depth=0)
    standings.Standings.model_rebuild(_parent_namespace_depth=0)
    league_list_response.LeagueListResponse.model_rebuild(_parent_namespace_depth=0)
    schedule_item_list_response.ScheduleItemListResponse.model_rebuild(_parent_namespace_depth=0)
    team_list_response.TeamListResponse.model_rebuild(_parent_namespace_depth=0)
    player_list_response.PlayerListResponse.model_rebuild(_parent_namespace_depth=0)
