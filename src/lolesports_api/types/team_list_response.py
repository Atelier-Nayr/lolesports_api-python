# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .schedule_item import ScheduleItem
from .highlander_team import HighlanderTeam
from .highlander_player import HighlanderPlayer

__all__ = [
    "TeamListResponse",
    "Player",
    "TeamRosterStat",
    "TeamStatsHistory",
    "TeamStatsSummary",
    "TeamStatsSummaryAverageDamageByPosition",
]


class Player(HighlanderPlayer):
    team_roster_stat: Optional[str] = FieldInfo(alias="teamRosterStat", default=None)


class TeamRosterStat(BaseModel):
    average_assists: int = FieldInfo(alias="averageAssists")

    average_deaths: float = FieldInfo(alias="averageDeaths")

    average_kill_participation: float = FieldInfo(alias="averageKillParticipation")

    average_kills: float = FieldInfo(alias="averageKills")

    champion_ids: List[int] = FieldInfo(alias="championIds")

    games_played: int = FieldInfo(alias="gamesPlayed")

    player_id: str = FieldInfo(alias="playerId")

    summoner_name: str = FieldInfo(alias="summonerName")


class TeamStatsHistory(BaseModel):
    id: str
    """Contains the game ID and the team ID."""

    assists: int

    game: int
    """The game ID"""

    kills: int

    match: str
    """The match ID"""

    opponent: int
    """The opponent's team ID"""

    team: int
    """The team ID"""

    timestamp: int
    """Unix timestamp in milliseconds of when the match started."""

    win: Literal[True, False]

    champion_ids: Optional[List[int]] = FieldInfo(alias="championIds", default=None)


class TeamStatsSummaryAverageDamageByPosition(BaseModel):
    duo: Optional[int] = FieldInfo(alias="DUO", default=None)

    duo_carry: Optional[int] = FieldInfo(alias="DUO_CARRY", default=None)

    duo_support: Optional[int] = FieldInfo(alias="DUO_SUPPORT", default=None)

    none: Optional[int] = FieldInfo(alias="NONE", default=None)

    solo: Optional[int] = FieldInfo(alias="SOLO", default=None)


class TeamStatsSummary(BaseModel):
    average_damage_by_position: TeamStatsSummaryAverageDamageByPosition = FieldInfo(alias="averageDamageByPosition")
    """It is assumed that the values represent the damage dealt in thousands."""

    average_win_length: int = FieldInfo(alias="averageWinLength")
    """The average length of the team's wins in seconds."""

    average_win_length_rank: int = FieldInfo(alias="averageWinLengthRank")
    """The position the team ranks at compared to other team's average win lengths."""

    first_dragon_kill_ratio: float = FieldInfo(alias="firstDragonKillRatio")
    """
    The ratio of first dragons killed by this team compared to the total first
    dragons killed in this team's matches.
    """

    first_dragon_kill_ratio_rank: int = FieldInfo(alias="firstDragonKillRatioRank")
    """
    The position the teams ranks at compared to other team's first dragon kill ratio
    """

    first_tower_ratio: float = FieldInfo(alias="firstTowerRatio")
    """
    The ratio of first tower secured by this team compared to the total first towers
    secured in this team's matches.
    """

    first_tower_ratio_rank: int = FieldInfo(alias="firstTowerRatioRank")
    """The position the teams ranks at compared to other team's first tower ratio."""

    kda_ratio: float = FieldInfo(alias="kdaRatio")
    """The team's KDA Ratio"""

    kda_ratio_rank: int = FieldInfo(alias="kdaRatioRank")
    """The position the team ranks at compared to other teams' KDA ratio"""

    team_id: str = FieldInfo(alias="teamId")
    """Contains the team ID"""


class TeamListResponse(BaseModel):
    highlander_tournaments: List["HighlanderTournament"] = FieldInfo(alias="highlanderTournaments")

    players: List[Player]
    """Contains the players currently in the team."""

    schedule_items: List[ScheduleItem] = FieldInfo(alias="scheduleItems")
    """Contains details about a few of the team's upcoming matches"""

    teams: List[HighlanderTeam]
    """An array containing the teams that have participated in this league."""

    team_roster_stats: Optional[List[TeamRosterStat]] = FieldInfo(alias="teamRosterStats", default=None)
    """
    Contains stats of the players of the particular team who played in that
    tournament.
    """

    team_stats_histories: Optional[List[TeamStatsHistory]] = FieldInfo(alias="teamStatsHistories", default=None)
    """
    A contains stats of the team's previous 4 matches in that particular tournament.
    """

    team_stats_summaries: Optional[List[TeamStatsSummary]] = FieldInfo(alias="teamStatsSummaries", default=None)
    """Contains a summary of the team stats during that particular tournament."""


from .highlander_tournament import HighlanderTournament
