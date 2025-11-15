# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VideoListResponse", "Video"]


class Video(BaseModel):
    id: int

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when this entry was created."""

    game: str
    """The game Id of the match.

    It is a
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    label: Optional[str] = None

    locale: str
    """The video's locale.

    The value is a [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language
    code.
    """

    reference: str
    """Contains the tournament Id and the game Id of that match."""

    slug: Optional[str] = None

    source: str
    """URL to the YouTube video of the match"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when this entry was last updated."""


class VideoListResponse(BaseModel):
    videos: List[Video]
