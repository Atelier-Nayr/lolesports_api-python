# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from . import foreign_ids
from .._models import BaseModel

__all__ = ["HighlanderPlayer", "Champion", "ForeignIDs"]


class Champion(BaseModel):
    id: int

    champion_id: int = FieldInfo(alias="championId")
    """The champion ID"""

    champion_key: str = FieldInfo(alias="championKey")
    """The champion's name"""

    champion_name: str = FieldInfo(alias="championName")
    """The champion's name"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when this entry was created."""

    player_id: int = FieldInfo(alias="playerId")
    """The player ID"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when this entry was last updated."""


class ForeignIDs(foreign_ids.ForeignIDs):
    """'This object may contain keys which are the names of various tournament realms.

    **Example:** `ESPORTSTMNT02: "200008392"`

    The purpose of the value in those strings is unknown.'
    """

    pass


class HighlanderPlayer(BaseModel):
    id: int
    """The player ID"""

    bios: Dict[str, str]
    """Contains a description of the player translated to various languages.

    The keys are presented in the format
    ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))

    `{languageCode}_{countryCode}`

    The value is a string containing html tags representing the description in that
    specific locale.
    """

    birthdate: Optional[datetime] = None

    champions: List[Champion]

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when this entry was created."""

    first_name: str = FieldInfo(alias="firstName")

    foreign_ids: ForeignIDs = FieldInfo(alias="foreignIds")
    """'This object may contain keys which are the names of various tournament realms.

    **Example:** `ESPORTSTMNT02: "200008392"`

    The purpose of the value in those strings is unknown.'
    """

    hometown: Optional[str] = None

    name: str
    """The player's in game name"""

    photo_url: Optional[str] = FieldInfo(alias="photoUrl", default=None)
    """URL to the player's photo"""

    region: str

    role_slug: str = FieldInfo(alias="roleSlug")
    """The role they usually play"""

    slug: str
    """URL friendly version of the player's in game name"""

    social_networks: Dict[str, str] = FieldInfo(alias="socialNetworks")
    """Contains links to the player's social media accounts.

    The key is the name of the social media platform and the value is the URL
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when this entry was last updated."""

    last_name: Optional[str] = FieldInfo(alias="LastName", default=None)
