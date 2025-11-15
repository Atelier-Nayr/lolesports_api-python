# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .participant_id import ParticipantID

__all__ = ["ParticipantStats"]


class ParticipantStats(BaseModel):
    assists: int

    creep_score: int = FieldInfo(alias="creepScore")

    current_health: int = FieldInfo(alias="currentHealth")

    deaths: int

    kills: int

    level: int

    max_health: int = FieldInfo(alias="maxHealth")

    participant_id: ParticipantID = FieldInfo(alias="participantId")

    total_gold: int = FieldInfo(alias="totalGold")
