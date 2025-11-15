# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .foreign_ids import ForeignIDs

__all__ = ["HighlanderTeam"]


class HighlanderTeam(BaseModel):
    id: int
    """The team ID."""

    acronym: str
    """The acronym form of the team name"""

    alt_logo_url: Optional[str] = FieldInfo(alias="altLogoUrl", default=None)
    """Alternative URL to the team's logo."""

    bios: Dict[str, str]
    """Contains a description of the team translated to various languages.

    The keys are presented in the format
    ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))

    `{languageCode}_{countryCode}`

    The value is a string containing html tags representing the description in that
    specific locale.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when this entry was created."""

    foreign_ids: ForeignIDs = FieldInfo(alias="foreignIds")

    guid: str
    """The team's [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)."""

    home_league: str = FieldInfo(alias="homeLeague")
    """Describes the league this team participates in during the regular seasons."""

    logo_url: str = FieldInfo(alias="logoUrl")
    """URL to an image of the team's logo."""

    name: str
    """The team name."""

    players: List[int]
    """An array containing the player IDs for those belonging in that team."""

    slug: str
    """URL friendly version of the team name."""

    starters: List[int]
    """An array of the player IDs of those in the main roster"""

    subs: List[int]
    """An array of the player IDs of the subs."""

    team_photo_url: Optional[str] = FieldInfo(alias="teamPhotoUrl", default=None)

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when this entry was last updated."""
