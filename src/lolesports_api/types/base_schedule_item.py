# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BaseScheduleItem", "Tags"]


class Tags(BaseModel):
    """
    The labels are used to describe the week and day the match/event is taking place in.
    Also, it could indicate the stage of the tournament.

    The blockPrefix comes before the block Label. Same with the subBlockPrefix and the subBlockLabel.
    """

    block_label: str = FieldInfo(alias="blockLabel")

    league_label: str = FieldInfo(alias="leagueLabel")

    sub_block_label: str = FieldInfo(alias="subBlockLabel")

    sub_block_prefix: str = FieldInfo(alias="subBlockPrefix")

    tournament_label: str = FieldInfo(alias="tournamentLabel")
    """Contains the tournament ID."""

    block_prefix: Optional[str] = FieldInfo(alias="blockPrefix", default=None)

    stage_label: Optional[str] = FieldInfo(alias="stageLabel", default=None)
    """Contains the tournament and bracket Ids the match/event belongs to."""

    year_label: Optional[str] = FieldInfo(alias="yearLabel", default=None)


class BaseScheduleItem(BaseModel):
    id: str
    """The schedule item ID."""

    league: str
    """The League ID"""

    scheduled_time: datetime = FieldInfo(alias="scheduledTime")
    """The time the match/event is/was scheduled to start."""

    tags: Tags
    """
    The labels are used to describe the week and day the match/event is taking place
    in. Also, it could indicate the stage of the tournament.

    The blockPrefix comes before the block Label. Same with the subBlockPrefix and
    the subBlockLabel.
    """

    tournament: str
    """The tournament ID"""
