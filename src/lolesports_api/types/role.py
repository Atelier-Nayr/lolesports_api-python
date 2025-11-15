# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Role"]


class Role(BaseModel):
    admin: Literal[True]

    origin: Literal["BEARER_TOKEN"]

    profile_icon_id: Literal[0] = FieldInfo(alias="profileIconId")

    region: Literal["global"]

    summoner_level: Literal[0] = FieldInfo(alias="summonerLevel")

    summoner_name: Literal["test-user"] = FieldInfo(alias="summonerName")
