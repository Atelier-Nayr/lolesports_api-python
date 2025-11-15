# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .schedule_item import ScheduleItem
from .highlander_team import HighlanderTeam
from .highlander_player import HighlanderPlayer
from .highlander_record import HighlanderRecord

__all__ = ["ScheduleItemListResponse"]


class ScheduleItemListResponse(BaseModel):
    highlander_records: Optional[List[HighlanderRecord]] = FieldInfo(alias="highlanderRecords", default=None)

    highlander_tournaments: Optional[List["HighlanderTournament"]] = FieldInfo(
        alias="highlanderTournaments", default=None
    )

    players: Optional[List[HighlanderPlayer]] = None

    schedule_items: Optional[List[ScheduleItem]] = FieldInfo(alias="scheduleItems", default=None)

    teams: Optional[List[HighlanderTeam]] = None
    """An array containing the teams that have participated in this league."""


from .highlander_tournament import HighlanderTournament
