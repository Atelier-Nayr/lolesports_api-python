# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .participant_stats import ParticipantStats

__all__ = ["TeamStats"]


class TeamStats(BaseModel):
    barons: int

    dragons: List[Literal["ocean", "mountain", "infernal", "cloud", "elder"]]

    inhibitors: int

    participants: List[ParticipantStats]

    total_gold: int = FieldInfo(alias="totalGold")

    total_kills: int = FieldInfo(alias="totalKills")

    towers: int
