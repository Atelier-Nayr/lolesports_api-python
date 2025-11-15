# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Team"]


class Team(BaseModel):
    code: str

    image: str

    name: str
