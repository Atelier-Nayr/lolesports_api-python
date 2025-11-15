# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DetailRetrieveParams"]


class DetailRetrieveParams(TypedDict, total=False):
    participant_ids: Annotated[str, PropertyInfo(alias="participantIds")]
    """A list of the participant Ids separated by underscores and not commas"""

    starting_time: Annotated[Union[str, datetime], PropertyInfo(alias="startingTime", format="iso8601")]
    """The date-time (RFC3339)"""
