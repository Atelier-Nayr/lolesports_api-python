# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .record import Record
from .outcome import Outcome
from .._models import BaseModel
from .base_league import BaseLeague
from .extended_event import ExtendedEvent

__all__ = [
    "GetScheduleRetrieveResponse",
    "Data",
    "DataSchedule",
    "DataScheduleEvent",
    "DataScheduleEventMatch",
    "DataScheduleEventMatchTeam",
    "DataScheduleEventMatchTeamResult",
    "DataSchedulePages",
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


class DataScheduleEventMatch(BaseModel):
    teams: List[DataScheduleEventMatchTeam]


class DataScheduleEvent(ExtendedEvent):
    league: BaseLeague

    match: DataScheduleEventMatch  # type: ignore


class DataSchedulePages(BaseModel):
    newer: Optional[str] = None
    """Base 64 encoded string used to determine the next "page" of data to pull"""

    older: Optional[str] = None
    """Base 64 encoded string used to determine the next "page" of data to pull"""


class DataSchedule(BaseModel):
    events: List[DataScheduleEvent]

    pages: DataSchedulePages

    updated: datetime
    """The time the data presented was last updated"""


class Data(BaseModel):
    schedule: DataSchedule


class GetScheduleRetrieveResponse(BaseModel):
    data: Data
