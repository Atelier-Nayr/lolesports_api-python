# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .state import State
from .._models import BaseModel
from .extended_vod import ExtendedVod

__all__ = ["SimpleGame"]


class SimpleGame(BaseModel):
    id: str
    """The game ID"""

    number: Literal[1, 2, 3, 4, 5]
    """The number of the game"""

    state: State

    vods: List[ExtendedVod]
