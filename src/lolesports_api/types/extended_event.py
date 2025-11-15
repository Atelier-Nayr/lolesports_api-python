# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .state import State
from .event_type import EventType
from .simple_event import SimpleEvent

__all__ = ["ExtendedEvent"]


class ExtendedEvent(SimpleEvent):
    state: State

    type: EventType
