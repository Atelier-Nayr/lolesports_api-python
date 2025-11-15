# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .base_league import BaseLeague

__all__ = ["HighlanderLeague"]


class HighlanderLeague(BaseLeague):
    id: int
    """The league's ID"""

    abouts: Dict[str, str]
    """Contains a description of the league translated in various languages.

    The keys are presented in the format
    ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))

    `{languageCode}_{countryCode}`

    The value is a string containing html tags representing the description in that
    specific locale.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when this entry was created."""

    drupal_id: Optional[int] = FieldInfo(alias="drupalId", default=None)

    guid: str
    """
    The [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) for the
    league.
    """

    logo_url: str = FieldInfo(alias="logoUrl")

    names: Dict[str, str]
    """Contains the names of the league translated in various languages.

    The keys are presented in the format
    ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))

    `{languageCode}_{countryCode}`

    The value is a string containing the name of the league in that specific locale.
    """

    region: str

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when this entry was last updated."""

    tournaments: Optional[List[str]] = None
    """
    An array containing the
    [UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) for the
    tournaments in this league.
    """
