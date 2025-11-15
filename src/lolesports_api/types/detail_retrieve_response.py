# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .base_frame import BaseFrame
from .participant_stats import ParticipantStats

__all__ = ["DetailRetrieveResponse", "Frame", "FrameParticipant", "FrameParticipantPerkMetadata"]


class FrameParticipantPerkMetadata(BaseModel):
    perks: List[int]
    """The runes selected.

    Index 0 - 3 are the ids of the primary runes Index 4 - 5 are the ids of the
    secondary runes Index 6 - 8 are the ids of the stats shard
    """

    style_id: Literal[8000, 8100, 8200, 8300, 8400] = FieldInfo(alias="styleId")
    """The id of the primary rune path"""

    sub_style_id: Literal[8000, 8100, 8200, 8300, 8400] = FieldInfo(alias="subStyleId")
    """The id of the secondary rune path"""


class FrameParticipant(ParticipantStats):
    abilities: List[str]
    """Contains the abilities the summoner levelled up at each level"""

    ability_power: int = FieldInfo(alias="abilityPower")

    armor: int

    attack_damage: int = FieldInfo(alias="attackDamage")

    attack_speed: int = FieldInfo(alias="attackSpeed")

    champion_damage_share: float = FieldInfo(alias="championDamageShare")

    critical_chance: float = FieldInfo(alias="criticalChance")

    items: List[int]
    """Contains the item Ids of the items in the inventory"""

    kill_participation: float = FieldInfo(alias="killParticipation")

    life_steal: int = FieldInfo(alias="lifeSteal")

    magic_resistance: int = FieldInfo(alias="magicResistance")

    perk_metadata: FrameParticipantPerkMetadata = FieldInfo(alias="perkMetadata")

    tenacity: float

    total_gold_earned: int = FieldInfo(alias="totalGoldEarned")

    wards_destroyed: int = FieldInfo(alias="wardsDestroyed")

    wards_placed: int = FieldInfo(alias="wardsPlaced")


class Frame(BaseFrame):
    participants: List[FrameParticipant]


class DetailRetrieveResponse(BaseModel):
    frames: List[Frame]
