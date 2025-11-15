# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .team import Team
from .._models import BaseModel

__all__ = ["BaseMatch"]


class BaseMatch(BaseModel):
    teams: List[Team]
