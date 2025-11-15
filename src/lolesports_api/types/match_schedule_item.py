# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .base_schedule_item import BaseScheduleItem

__all__ = ["MatchScheduleItem"]


class MatchScheduleItem(BaseScheduleItem):
    bracket: str
    """The bracket ID"""

    content: str
    """Contains the tournament and match Ids for the specific match."""

    match: str
    """The match ID"""
