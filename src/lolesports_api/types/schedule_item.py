# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .base_schedule_item import BaseScheduleItem
from .match_schedule_item import MatchScheduleItem

__all__ = ["ScheduleItem", "EventScheduleItem"]


class EventScheduleItem(BaseScheduleItem):
    content: str


ScheduleItem: TypeAlias = Union[MatchScheduleItem, EventScheduleItem]
