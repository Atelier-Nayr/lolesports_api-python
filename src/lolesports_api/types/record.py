# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Record"]


class Record(BaseModel):
    """
    Describes the amount of wins and losses the team has incurred
    in a particular stage of the tournament specifically group stage

    For knockout phase, each series is treated individually.

    This object is null when the match is ongoing and it is in the
    knockout stage.
    """

    losses: int

    wins: int
