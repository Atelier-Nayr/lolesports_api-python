# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .base_frame import BaseFrame
from .team_stats import TeamStats
from .team_metadata import TeamMetadata

__all__ = ["WindowRetrieveResponse", "Frame", "GameMetadata"]


class Frame(BaseFrame):
    blue_team: TeamStats = FieldInfo(alias="blueTeam")

    game_state: Literal["in_game", "finished"] = FieldInfo(alias="gameState")

    red_team: TeamStats = FieldInfo(alias="redTeam")

    rfc460_timestamp: datetime = FieldInfo(alias="rfc460Timestamp")  # type: ignore


class GameMetadata(BaseModel):
    blue_team_metadata: TeamMetadata = FieldInfo(alias="blueTeamMetadata")

    patch_version: str = FieldInfo(alias="patchVersion")
    """The patch the match was played on"""

    red_team_metadata: TeamMetadata = FieldInfo(alias="redTeamMetadata")


class WindowRetrieveResponse(BaseModel):
    esports_game_id: str = FieldInfo(alias="esportsGameId")
    """The game Id of the match"""

    esports_match_id: str = FieldInfo(alias="esportsMatchId")
    """The match Id of the match"""

    frames: List[Frame]

    game_metadata: GameMetadata = FieldInfo(alias="gameMetadata")
