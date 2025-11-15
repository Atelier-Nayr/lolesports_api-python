# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScheduleItemListParams"]


class ScheduleItemListParams(TypedDict, total=False):
    league_id: Required[Annotated[int, PropertyInfo(alias="leagueId")]]
    """The id of the league you want details of"""
