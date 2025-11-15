# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GetTournamentsForLeagueListResponse", "Data", "DataLeague", "DataLeagueTournament"]


class DataLeagueTournament(BaseModel):
    id: str
    """This is the tournament id"""

    end_date: str = FieldInfo(alias="endDate")
    """The date the tournament ends/ended."""

    slug: str

    start_date: str = FieldInfo(alias="startDate")
    """The date the tournament starts/started."""


class DataLeague(BaseModel):
    tournaments: List[DataLeagueTournament]
    """
    An array of tournament object(s) where each object describes a specific
    tournament.
    """


class Data(BaseModel):
    leagues: List[DataLeague]
    """
    An array of league object(s) where each object contains an array of tournaments.
    """


class GetTournamentsForLeagueListResponse(BaseModel):
    data: Data
