# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .result import Result
from .._models import BaseModel
from .event_type import EventType
from .simple_game import SimpleGame
from .extended_vod import ExtendedVod
from .base_strategy import BaseStrategy
from .simple_league import SimpleLeague

__all__ = [
    "GetEventDetailRetrieveResponse",
    "Data",
    "DataEvent",
    "DataEventMatch",
    "DataEventMatchGame",
    "DataEventMatchGameTeam",
    "DataEventMatchTeam",
]


class DataEventMatchGameTeam(BaseModel):
    id: str
    """The team id"""

    side: Literal["blue", "red"]


class DataEventMatchGame(SimpleGame):
    teams: List[DataEventMatchGameTeam]


class DataEventMatchTeam(BaseModel):
    id: str
    """The team id"""

    code: str

    image: str

    name: str

    result: Result


class DataEventMatch(BaseModel):
    games: List[DataEventMatchGame]

    strategy: BaseStrategy

    teams: List[DataEventMatchTeam]


class DataEvent(BaseModel):
    id: str

    league: SimpleLeague

    match: DataEventMatch

    streams: Optional[List[ExtendedVod]] = None
    """
    For a live match this will contain information about various streams, the
    platforms they are on and the locale.

    Otherwise it will be null.
    """

    type: EventType


class Data(BaseModel):
    event: DataEvent


class GetEventDetailRetrieveResponse(BaseModel):
    data: Data
