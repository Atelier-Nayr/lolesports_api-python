# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .highlander_team import HighlanderTeam
from .highlander_league import HighlanderLeague
from .highlander_player import HighlanderPlayer
from .highlander_record import HighlanderRecord

__all__ = ["LeagueListResponse"]


class LeagueListResponse(BaseModel):
    leagues: List[HighlanderLeague]
    """This array contains information about the league retrieved."""

    highlander_records: Optional[List[HighlanderRecord]] = FieldInfo(alias="highlanderRecords", default=None)

    highlander_tournaments: Optional[List["HighlanderTournament"]] = FieldInfo(
        alias="highlanderTournaments", default=None
    )

    players: Optional[List[HighlanderPlayer]] = None

    teams: Optional[List[HighlanderTeam]] = None
    """An array containing the teams that have participated in this league."""


from .highlander_tournament import HighlanderTournament
