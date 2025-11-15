# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TeamListParams"]


class TeamListParams(TypedDict, total=False):
    slug: Required[str]
    """The team slug."""

    tournament: Required[str]
    """The tournament ID."""
