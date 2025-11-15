# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Result"]


class Result(BaseModel):
    game_wins: int = FieldInfo(alias="gameWins")
    """The number of games the team has won in that in the series"""
