# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo

__all__ = ["GetScheduleRetrieveParams"]


class GetScheduleRetrieveParams(TypedDict, total=False):
    hl: Required[
        Literal[
            "en-US",
            "en-GB",
            "en-AU",
            "cs-CZ",
            "de-DE",
            "el-GR",
            "es-ES",
            "es-MX",
            "fr-FR",
            "hu-HU",
            "it-IT",
            "pl-PL",
            "pt-BR",
            "ro-RO",
            "ru-RU",
            "tr-TR",
            "ja-JP",
            "ko-KR",
        ]
    ]
    """
    This is the locale or language code using
    [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) and
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
    """

    league_id: Annotated[Iterable[int], PropertyInfo(alias="leagueId")]
    """The id(s) of the league(s) you want details of"""

    page_token: Annotated[Union[str, Base64FileInput], PropertyInfo(alias="pageToken", format="base64")]
    """Base 64 encoded string used to determine the next "page" of data to pull"""
