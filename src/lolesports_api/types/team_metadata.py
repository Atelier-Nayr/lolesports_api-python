# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from . import participant_metadata
from .._models import BaseModel

__all__ = ["TeamMetadata", "ParticipantMetadata", "ParticipantMetadataParticipantMetadataExtended"]


class ParticipantMetadataParticipantMetadataExtended(participant_metadata.ParticipantMetadata):
    esports_player_id: str = FieldInfo(alias="esportsPlayerId")


ParticipantMetadata: TypeAlias = Union[
    participant_metadata.ParticipantMetadata, ParticipantMetadataParticipantMetadataExtended
]


class TeamMetadata(BaseModel):
    esports_team_id: str = FieldInfo(alias="esportsTeamId")
    """The team Id"""

    participant_metadata: List[ParticipantMetadata] = FieldInfo(alias="participantMetadata")
