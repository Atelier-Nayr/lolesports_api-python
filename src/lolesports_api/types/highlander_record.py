# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["HighlanderRecord"]


class HighlanderRecord(BaseModel):
    id: str
    """A combination of the bracket and roster UUIDs.

    The two are separated by a colon\\
    """

    bracket: str
    """
    The bracket's
    [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    losses: int

    roster: str
    """
    The roster's [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    score: int

    ties: int

    tournament: str
    """
    The tournament's
    [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    wins: int
