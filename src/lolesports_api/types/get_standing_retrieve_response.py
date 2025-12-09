# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .team import Team
from .state import State
from .record import Record
from .result import Result
from .outcome import Outcome
from .._models import BaseModel
from .simple_match import SimpleMatch

__all__ = [
    "GetStandingRetrieveResponse",
    "Data",
    "DataStanding",
    "DataStandingStage",
    "DataStandingStageSection",
    "DataStandingStageSectionMatch",
    "DataStandingStageSectionMatchTeam",
    "DataStandingStageSectionMatchTeamResult",
    "DataStandingStageSectionRanking",
    "DataStandingStageSectionRankingTeam",
]


class DataStandingStageSectionMatchTeamResult(Result):
    outcome: Optional[Outcome] = None
    """Indicate whether the team won or lost the series

    This will be null if the match is ongoing
    """


class DataStandingStageSectionMatchTeam(BaseModel):
    id: str
    """The team id"""

    result: DataStandingStageSectionMatchTeamResult

    slug: str
    """The URL friendly version of the team name"""


class DataStandingStageSectionMatch(SimpleMatch):
    flags: Optional[str] = None
    """The purpose of this key is unknown.

    So far the only value it has seems to be null.
    """

    previous_match_ids: Optional[List[str]] = FieldInfo(alias="previousMatchIds", default=None)
    """
    This stores the previous match ids for the teams in the current match were
    involved in.

    For group stages this is usually null. For bracket stage it is used to indicate
    the matches that were played before the match in question.
    """

    state: State

    teams: List[DataStandingStageSectionMatchTeam]  # type: ignore


class DataStandingStageSectionRankingTeam(Team):
    id: Optional[str] = None
    """The team id"""

    record: Optional[Record] = None
    """
    Describes the amount of wins and losses the team has incurred in a particular
    stage of the tournament specifically group stage

    For knockout phase, each series is treated individually.

    This object is null when the match is ongoing and it is in the knockout stage.
    """

    slug: Optional[str] = None
    """The URL friendly version of the team name"""


class DataStandingStageSectionRanking(BaseModel):
    ordinal: int
    """The league position"""

    teams: List[DataStandingStageSectionRankingTeam]
    """The teams that are at that league position.

    In most cases there will only be one team object in this array. In cases where
    several teams are tied with the same score, this array will contain all teams
    tied for that position.
    """


class DataStandingStageSection(BaseModel):
    matches: List[DataStandingStageSectionMatch]

    name: str
    """The name of the section"""

    rankings: List[DataStandingStageSectionRanking]
    """Contains details about the actual standings for that particular section

    This is mostly used for the group stage. For the knockout stages, it is usually
    empty.
    """


class DataStandingStage(BaseModel):
    """Represents a stage in a tournament.

    Whether it is the group or knockout stage.
    """

    name: str
    """The name of that stage of the tournament"""

    sections: List[DataStandingStageSection]
    """
    Each object in the array represents a particular round in that specific stage in
    the tournament.

    For the knockout stages, we could have the quarter finals, semi finals and the
    finals under their own sections.

    For the group stage, there is usually only one section.
    """

    slug: str

    type: Literal["groups", "bracket"]
    """The type of the stage."""


class DataStanding(BaseModel):
    stages: List[DataStandingStage]


class Data(BaseModel):
    standings: List[DataStanding]
    """Each object in the array contains details of each tournament requested."""


class GetStandingRetrieveResponse(BaseModel):
    data: Data
