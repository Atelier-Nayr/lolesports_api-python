# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .vod import Vod
from .._models import BaseModel
from .simple_event import SimpleEvent

__all__ = [
    "GetCompletedEventListResponse",
    "Data",
    "DataSchedule",
    "DataScheduleEvent",
    "DataScheduleEventGame",
    "DataScheduleEventMatch",
]


class DataScheduleEventGame(BaseModel):
    vods: List[Vod]


class DataScheduleEventMatch(BaseModel):
    type: Literal["normal"]


class DataScheduleEvent(SimpleEvent):
    games: List[DataScheduleEventGame]

    match: DataScheduleEventMatch  # type: ignore


class DataSchedule(BaseModel):
    events: List[DataScheduleEvent]


class Data(BaseModel):
    schedule: DataSchedule


class GetCompletedEventListResponse(BaseModel):
    data: Data
