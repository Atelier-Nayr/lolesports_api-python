# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .result import Result
from .._models import BaseModel
from .simple_match import SimpleMatch
from .base_strategy import BaseStrategy

__all__ = ["SimpleEvent", "Match", "MatchStrategy", "MatchTeam"]


class MatchStrategy(BaseStrategy):
    type: Literal["bestOf"]


class MatchTeam(BaseModel):
    result: Result


class Match(SimpleMatch):
    strategy: MatchStrategy

    teams: List[MatchTeam]  # type: ignore


class SimpleEvent(BaseModel):
    block_name: Optional[str] = FieldInfo(alias="blockName", default=None)

    match: Match

    start_time: datetime = FieldInfo(alias="startTime")
    """The time the match started"""
