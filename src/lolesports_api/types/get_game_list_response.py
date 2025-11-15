# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .simple_game import SimpleGame

__all__ = ["GetGameListResponse", "Data"]


class Data(BaseModel):
    games: List[SimpleGame]


class GetGameListResponse(BaseModel):
    data: Data
