# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .highlander_league import HighlanderLeague

__all__ = ["NavItemListResponse"]


class NavItemListResponse(BaseModel):
    leagues: List[HighlanderLeague]

    nav_items: List["NavItem"] = FieldInfo(alias="navItems")


from .nav_item import NavItem
