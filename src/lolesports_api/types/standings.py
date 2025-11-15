# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Standings", "Result"]


class Result(BaseModel):
    roster: Optional[str] = None
    """The roster ID"""


class Standings(BaseModel):
    closed: Literal[True, False]
    """
    If the value is true then the league/tournament has concluded, otherwise it is
    ongoing.
    """

    result: List[List[Result]]

    timestamp: int
    """Unix timestamp in milliseconds of when the match started."""

    history: Optional[List["Standings"]] = None

    note: Optional[str] = None

    source: Optional[Literal["manual", "bestOf"]] = None
    """How the record was created/updated."""
