# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .base_league import BaseLeague

__all__ = ["SimpleLeague"]


class SimpleLeague(BaseLeague):
    id: str
    """The league's ID"""

    image: str
    """URL to an image of the League's logo"""
