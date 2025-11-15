# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BaseLeague"]


class BaseLeague(BaseModel):
    name: str
    """The name of the league"""

    slug: str
    """URL friendly version of the league's name"""
