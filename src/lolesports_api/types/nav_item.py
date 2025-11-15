# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NavItem", "ParentNavItem"]


class ParentNavItem(NavItem):
    pass


class NavItem(BaseModel):
    id: int

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when this entry was created."""

    external: bool

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    label: str

    link: str

    order: int

    parent_nav_item: ParentNavItem = FieldInfo(alias="parentNavItem")

    slug: Optional[str] = None

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when this entry was last updated."""
