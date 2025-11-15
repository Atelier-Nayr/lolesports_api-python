# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .extended_league import ExtendedLeague

__all__ = ["GetLeagueListResponse", "Data", "DataLeague"]


class DataLeague(ExtendedLeague):
    region: str
    """Indicates which type of tournament the league is.

    Whether international or a regional tournament. The region name is given.
    """


class Data(BaseModel):
    leagues: List[DataLeague]


class GetLeagueListResponse(BaseModel):
    data: Data
