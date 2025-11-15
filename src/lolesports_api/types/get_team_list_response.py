# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .team import Team
from .._models import BaseModel

__all__ = ["GetTeamListResponse", "Data", "DataTeam", "DataTeamHomeLeague", "DataTeamPlayer"]


class DataTeamHomeLeague(BaseModel):
    name: str
    """The name of the league"""

    region: str
    """The region where the league is located"""


class DataTeamPlayer(BaseModel):
    id: str

    first_name: str = FieldInfo(alias="firstName")

    image: str

    last_name: str = FieldInfo(alias="lastName")

    role: str

    summoner_name: str = FieldInfo(alias="summonerName")


class DataTeam(Team):
    id: str
    """The team id"""

    alternative_image: str = FieldInfo(alias="alternativeImage")

    home_league: DataTeamHomeLeague = FieldInfo(alias="homeLeague")

    players: List[DataTeamPlayer]

    slug: str
    """The URL friendly version of the team name"""


class Data(BaseModel):
    teams: List[DataTeam]


class GetTeamListResponse(BaseModel):
    data: Data
