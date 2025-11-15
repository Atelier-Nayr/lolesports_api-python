# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .highlander_team import HighlanderTeam
from .highlander_player import HighlanderPlayer
from .match_schedule_item import MatchScheduleItem

__all__ = [
    "PlayerListResponse",
    "Player",
    "PlayerPhotoInformation",
    "PlayerStatsHistory",
    "PlayerStatsSummary",
    "PlayerStatsSummaryMostplayedchampion",
]


class PlayerPhotoInformation(BaseModel):
    height: int
    """The height of the image in pixels."""

    size: int
    """Size of the image in bytes"""

    time: float

    transferred: int

    type: str
    """The image's file format."""

    url: str
    """URL to the player's photo."""

    width: int
    """The width of the image in pixels."""


class Player(HighlanderPlayer):
    photo_information: PlayerPhotoInformation = FieldInfo(alias="photoInformation")

    schedule_items: List[str] = FieldInfo(alias="scheduleItems")
    """
    Contains the ids to schedule items representing the player's/team's next
    matches.

    This is regardless of the tournament ID passed in the url.
    """

    starter_on_teams: List[int] = FieldInfo(alias="starterOnTeams")
    """The IDs of the team(s) this player is/has been on the starting lineup"""

    sub_on_teams: List[int] = FieldInfo(alias="subOnTeams")
    """The IDs of the team(s) this player is/has been on as a sub player"""

    teams: List[int]
    """A combination of the teamIDs in `starterOnTeams` and `subOnTeams`"""

    player_stats_history: Optional[List[str]] = FieldInfo(alias="playerStatsHistory", default=None)
    """
    Contains the `playerStatsHistory` IDs, which are just the game ID of the match
    and the player ID separated by a colon.

    Contains the last 4 played matches in the specified tournament. The first ID is
    of the most recently played match.
    """

    player_stats_summary: Optional[str] = FieldInfo(alias="playerStatsSummary", default=None)


class PlayerStatsHistory(BaseModel):
    id: str

    assists: float

    champion_id: float = FieldInfo(alias="championId")

    cs_per_ten_minutes: float = FieldInfo(alias="csPerTenMinutes")

    deaths: float

    game: str
    """The game ID"""

    kda_ratio: float = FieldInfo(alias="kdaRatio")

    kill_participation: float = FieldInfo(alias="killParticipation")

    kills: float

    match: str
    """The match ID"""

    opponent: float
    """The opponent's team ID."""

    player_id: str = FieldInfo(alias="playerId")

    team: float
    """The team ID the player playes for."""

    timestamp: int
    """Unix timestamp in milliseconds of when the match started."""

    win: Literal[True, False]


class PlayerStatsSummaryMostplayedchampion(BaseModel):
    champion_id: float = FieldInfo(alias="championId")

    kda_ratio: float = FieldInfo(alias="kdaRatio")

    losses: float

    total: float

    wins: float


class PlayerStatsSummary(BaseModel):
    cs_per_ten_minutes: float = FieldInfo(alias="csPerTenMinutes")

    cs_per_ten_minutes_rank: float = FieldInfo(alias="csPerTenMinutesRank")

    kda_ratio: float = FieldInfo(alias="kdaRatio")

    kda_ratio_rank: float = FieldInfo(alias="kdaRatioRank")

    kill_participation: float = FieldInfo(alias="killParticipation")

    kill_participation_rank: float = FieldInfo(alias="killParticipationRank")

    mostplayedchampions: List[PlayerStatsSummaryMostplayedchampion]

    player_id: str = FieldInfo(alias="playerId")


class PlayerListResponse(BaseModel):
    highlander_tournaments: List["HighlanderTournament"] = FieldInfo(alias="highlanderTournaments")
    """Contains the various tournaments the player has participated in."""

    players: List[Player]
    """Contains information about the player in question.

    If `playerStatsSummary` and `playerStatsHistory` are missing then the player did
    not take part in the tournament specificed by the tournament ID in the url.
    """

    schedule_items: List[MatchScheduleItem] = FieldInfo(alias="scheduleItems")
    """
    Contains details about the next 4 matches the player's team is schedule to
    participate in.
    """

    teams: List[HighlanderTeam]

    player_stats_histories: Optional[List[PlayerStatsHistory]] = FieldInfo(alias="playerStatsHistories", default=None)
    """
    Displays stats from the recently played matches in that particular tournaments.
    The array starts with the most recently played match.
    """

    player_stats_summaries: Optional[List[PlayerStatsSummary]] = FieldInfo(alias="playerStatsSummaries", default=None)
    """
    The stats displayed here are for the player during the tournament specified in
    the url
    """


from .highlander_tournament import HighlanderTournament
