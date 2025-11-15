# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .record import Record
from .outcome import Outcome
from .._models import BaseModel
from .extended_event import ExtendedEvent
from .extended_league import ExtendedLeague

__all__ = [
    "GetLiveRetrieveResponse",
    "Data",
    "DataSchedule",
    "DataScheduleEvent",
    "DataScheduleEventMatch",
    "DataScheduleEventMatchTeam",
    "DataScheduleEventMatchTeamResult",
]


class DataScheduleEventMatchTeamResult(BaseModel):
    outcome: Optional[Outcome] = None
    """Indicate whether the team won or lost the series

    This will be null if the match is ongoing
    """


class DataScheduleEventMatchTeam(BaseModel):
    record: Optional[Record] = None
    """
    Describes the amount of wins and losses the team has incurred in a particular
    stage of the tournament specifically group stage

    For knockout phase, each series is treated individually.

    This object is null when the match is ongoing and it is in the knockout stage.
    """

    result: DataScheduleEventMatchTeamResult

    slug: str
    """The URL friendly version of the team name"""


class DataScheduleEventMatch(BaseModel):
    teams: List[DataScheduleEventMatchTeam]


class DataScheduleEvent(ExtendedEvent):
    id: str

    league: ExtendedLeague

    match: Optional[DataScheduleEventMatch] = None  # type: ignore


class DataSchedule(BaseModel):
    events: Optional[List[DataScheduleEvent]] = None
    """Array of event objects representing matches that are currently ongoing.

    This will be null if no match is taking place at that time
    """


class Data(BaseModel):
    schedule: DataSchedule


class GetLiveRetrieveResponse(BaseModel):
    data: Data
