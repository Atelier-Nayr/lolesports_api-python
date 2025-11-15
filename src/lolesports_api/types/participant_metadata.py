# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .participant_id import ParticipantID

__all__ = ["ParticipantMetadata"]


class ParticipantMetadata(BaseModel):
    champion_id: str = FieldInfo(alias="championId")

    participant_id: ParticipantID = FieldInfo(alias="participantId")

    role: Literal["top", "jungle", "mid", "bottom", "support"]

    summoner_name: str = FieldInfo(alias="summonerName")
