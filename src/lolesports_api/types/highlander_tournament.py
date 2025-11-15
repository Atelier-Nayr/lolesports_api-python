# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .role import Role
from .._models import BaseModel
from .rostering_strategy import RosteringStrategy

__all__ = [
    "HighlanderTournament",
    "Brackets",
    "BracketsMatches",
    "BracketsMatchesGames",
    "BracketsMatchesGamesInput",
    "BracketsMatchesGamesInputUnionMember0",
    "BracketsMatchesGamesInputUnionMember1",
    "BracketsMatchesGamesRoles",
    "BracketsMatchesGamesGameMode",
    "BracketsMatchesInput",
    "BracketsMatchesInputUnionMember0",
    "BracketsMatchesInputUnionMember1",
    "BracketsMatchesRemadeGame",
    "BracketsMatchesRemadeGameInput",
    "BracketsMatchesRemadeGameInputUnionMember0",
    "BracketsMatchesRemadeGameInputUnionMember1",
    "BracketsMatchesRemadeGameRoles",
    "BracketsMatchesRemadeGameGameMode",
    "BracketsMatchesRoles",
    "BracketsMatchesGameMode",
    "BracketsMatchesMatchType",
    "BracketsMatchesMatchTypeOptions",
    "BracketsMatchesScoring",
    "BracketsMatchesScoringOptions",
    "BracketsRoles",
    "BracketsBracketType",
    "BracketsBracketTypeOptions",
    "BracketsGameMode",
    "BracketsInheritableMatchScoringStrategy",
    "BracketsInheritableMatchScoringStrategyOptions",
    "BracketsInput",
    "BracketsMatchScoring",
    "BracketsMatchScoringOptions",
    "BracketsMatchType",
    "BracketsMatchTypeOptions",
    "BracketsScoring",
    "BracketsScoringOptions",
    "Roles",
    "Rosters",
    "BracketType",
    "BracketTypeOptions",
    "Breakpoints",
    "BreakpointsGenerator",
    "BreakpointsInput",
    "BreakpointsRoles",
    "MatchType",
    "MatchTypeOptions",
]


class BracketsMatchesGamesInputUnionMember0(BaseModel):
    match: Optional[str] = None
    """The match ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


class BracketsMatchesGamesInputUnionMember1(BaseModel):
    breakpoint: Optional[str] = None
    """The breakpoint ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


BracketsMatchesGamesInput: TypeAlias = Union[
    BracketsMatchesGamesInputUnionMember0, BracketsMatchesGamesInputUnionMember1
]


class BracketsMatchesGamesRoles(BaseModel):
    creator: List[Role]

    owner: List[Role]


class BracketsMatchesGamesGameMode(BaseModel):
    identifier: Literal["lol:duel", "lol:classic"]

    map_name: Literal["summoner_rift", "howling_abyss"] = FieldInfo(alias="mapName")

    required_players: Literal[1, 5] = FieldInfo(alias="requiredPlayers")


class BracketsMatchesGames(BaseModel):
    id: str
    """The game Id of the match.

    It is a
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    generated_name: str = FieldInfo(alias="generatedName")

    input: List[BracketsMatchesGamesInput]

    name: str

    revision: int

    roles: BracketsMatchesGamesRoles

    scores: Dict[str, int]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """The numeric version of the game ID

    This is what is used to access the ACS endpoint.
    """

    game_mode: Optional[BracketsMatchesGamesGameMode] = FieldInfo(alias="gameMode", default=None)

    game_realm: Optional[str] = FieldInfo(alias="gameRealm", default=None)
    """The ID of the tournament realm on which the game was played on"""

    platform_id: Optional[str] = FieldInfo(alias="platformId", default=None)
    """A combination of the gameRealm and the gameId"""

    standings: Optional["Standings"] = None

    state: Optional[Literal["remade"]] = None


class BracketsMatchesInputUnionMember0(BaseModel):
    match: Optional[str] = None
    """The match ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


class BracketsMatchesInputUnionMember1(BaseModel):
    breakpoint: Optional[str] = None
    """The breakpoint ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


BracketsMatchesInput: TypeAlias = Union[BracketsMatchesInputUnionMember0, BracketsMatchesInputUnionMember1]


class BracketsMatchesRemadeGameInputUnionMember0(BaseModel):
    match: Optional[str] = None
    """The match ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


class BracketsMatchesRemadeGameInputUnionMember1(BaseModel):
    breakpoint: Optional[str] = None
    """The breakpoint ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


BracketsMatchesRemadeGameInput: TypeAlias = Union[
    BracketsMatchesRemadeGameInputUnionMember0, BracketsMatchesRemadeGameInputUnionMember1
]


class BracketsMatchesRemadeGameRoles(BaseModel):
    creator: List[Role]

    owner: List[Role]


class BracketsMatchesRemadeGameGameMode(BaseModel):
    identifier: Literal["lol:duel", "lol:classic"]

    map_name: Literal["summoner_rift", "howling_abyss"] = FieldInfo(alias="mapName")

    required_players: Literal[1, 5] = FieldInfo(alias="requiredPlayers")


class BracketsMatchesRemadeGame(BaseModel):
    id: str
    """The game Id of the match.

    It is a
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    generated_name: str = FieldInfo(alias="generatedName")

    input: List[BracketsMatchesRemadeGameInput]

    name: str

    revision: int

    roles: BracketsMatchesRemadeGameRoles

    scores: Dict[str, int]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """The numeric version of the game ID

    This is what is used to access the ACS endpoint.
    """

    game_mode: Optional[BracketsMatchesRemadeGameGameMode] = FieldInfo(alias="gameMode", default=None)

    game_realm: Optional[str] = FieldInfo(alias="gameRealm", default=None)
    """The ID of the tournament realm on which the game was played on"""

    platform_id: Optional[str] = FieldInfo(alias="platformId", default=None)
    """A combination of the gameRealm and the gameId"""

    standings: Optional["Standings"] = None

    state: Optional[Literal["remade"]] = None


class BracketsMatchesRoles(BaseModel):
    creator: List[Role]

    owner: List[Role]


class BracketsMatchesGameMode(BaseModel):
    identifier: Literal["lol:duel", "lol:classic"]

    map_name: Literal["summoner_rift", "howling_abyss"] = FieldInfo(alias="mapName")

    required_players: Literal[1, 5] = FieldInfo(alias="requiredPlayers")


class BracketsMatchesMatchTypeOptions(BaseModel):
    best_of: str


class BracketsMatchesMatchType(BaseModel):
    identifier: Literal["bestOf", "single_elim"]

    options: Optional[BracketsMatchesMatchTypeOptions] = None


class BracketsMatchesScoringOptions(BaseModel):
    points: List[int]


class BracketsMatchesScoring(BaseModel):
    identifier: Literal["standard", "LegacyScoringStrategy"]
    """
    **Note:** The `LegacyScoringStrategy` value has only been found in the 2015
    worlds championship.
    """

    options: BracketsMatchesScoringOptions


class BracketsMatches(BaseModel):
    id: str
    """The match ID"""

    games: Dict[str, BracketsMatchesGames]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the game ID.

    These are the games played in that series.

    The number of properties(key and value pair) in this object will be equal to the
    type of series that was played. For a best of 1 there will be only 1 game, 3 for
    best of 3s and 5 for best of 5s.
    """

    group_position: int = FieldInfo(alias="groupPosition")

    input: List[BracketsMatchesInput]

    name: str

    position: int

    remade_games: List[BracketsMatchesRemadeGame] = FieldInfo(alias="remadeGames")

    roles: BracketsMatchesRoles

    scores: Dict[str, int]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    state: Literal["resolved", "unresolved", "unlinked"]
    """Whether it is ongoing or completed."""

    tiebreaker: Literal[True, False]

    game_mode: Optional[BracketsMatchesGameMode] = FieldInfo(alias="gameMode", default=None)

    match_type: Optional[BracketsMatchesMatchType] = FieldInfo(alias="matchType", default=None)

    scoring: Optional[BracketsMatchesScoring] = None

    standings: Optional["Standings"] = None


class BracketsRoles(BaseModel):
    creator: List[Role]

    owner: List[Role]


class BracketsBracketTypeOptions(BaseModel):
    rounds: str


class BracketsBracketType(BaseModel):
    identifier: Literal["round_robin", "single_elim", "gauntlet", "bestOf"]

    options: Optional[BracketsBracketTypeOptions] = None


class BracketsGameMode(BaseModel):
    identifier: Literal["lol:duel", "lol:classic"]

    map_name: Literal["summoner_rift", "howling_abyss"] = FieldInfo(alias="mapName")

    required_players: Literal[1, 5] = FieldInfo(alias="requiredPlayers")


class BracketsInheritableMatchScoringStrategyOptions(BaseModel):
    points: List[int]


class BracketsInheritableMatchScoringStrategy(BaseModel):
    identifier: Literal["standard", "LegacyScoringStrategy"]
    """
    **Note:** The `LegacyScoringStrategy` value has only been found in the 2015
    worlds championship.
    """

    options: BracketsInheritableMatchScoringStrategyOptions


class BracketsInput(BaseModel):
    breakpoint: Optional[str] = None
    """The breakpoint ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


class BracketsMatchScoringOptions(BaseModel):
    points: List[int]


class BracketsMatchScoring(BaseModel):
    identifier: Literal["standard", "LegacyScoringStrategy"]
    """
    **Note:** The `LegacyScoringStrategy` value has only been found in the 2015
    worlds championship.
    """

    options: BracketsMatchScoringOptions


class BracketsMatchTypeOptions(BaseModel):
    best_of: str


class BracketsMatchType(BaseModel):
    identifier: Literal["bestOf", "single_elim"]

    options: Optional[BracketsMatchTypeOptions] = None


class BracketsScoringOptions(BaseModel):
    points: List[int]


class BracketsScoring(BaseModel):
    identifier: Literal["standard", "LegacyScoringStrategy"]
    """
    **Note:** The `LegacyScoringStrategy` value has only been found in the 2015
    worlds championship.
    """

    options: BracketsScoringOptions


class Brackets(BaseModel):
    id: str
    """The bracket ID."""

    can_manufacture: bool = FieldInfo(alias="canManufacture")

    group_position: int = FieldInfo(alias="groupPosition")

    matches: Dict[str, BracketsMatches]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the match ID.
    """

    match_scores: Dict[str, int] = FieldInfo(alias="matchScores")
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    name: str
    """The name of the bracket"""

    position: int

    roles: BracketsRoles

    scores: Dict[str, int]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    state: Literal["resolved", "unresolved", "unlinked"]
    """Whether it is ongoing or completed.

    This is unreliable since some tournaments have the state unresolved yet they
    concluded a long time ago.
    """

    bracket_type: Optional[BracketsBracketType] = FieldInfo(alias="bracketType", default=None)

    game_mode: Optional[BracketsGameMode] = FieldInfo(alias="gameMode", default=None)

    group_name: Optional[str] = FieldInfo(alias="groupName", default=None)

    inheritable_match_scoring_strategy: Optional[BracketsInheritableMatchScoringStrategy] = FieldInfo(
        alias="inheritableMatchScoringStrategy", default=None
    )

    input: Optional[List[BracketsInput]] = None

    match_scoring: Optional[BracketsMatchScoring] = FieldInfo(alias="matchScoring", default=None)

    match_type: Optional[BracketsMatchType] = FieldInfo(alias="matchType", default=None)

    scoring: Optional[BracketsScoring] = None

    standings: Optional["Standings"] = None


class Roles(BaseModel):
    creator: List[Role]

    owner: List[Role]


class Rosters(BaseModel):
    id: str
    """The roster ID.

    It is a
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    name: str
    """The abbreviated version of the team's name."""

    roles: object

    substitutions: object

    team: str
    """The Team ID"""

    team_reference: str = FieldInfo(alias="teamReference")

    state: Optional[Literal["eliminated"]] = None


class BracketTypeOptions(BaseModel):
    rounds: str


class BracketType(BaseModel):
    identifier: Literal["round_robin", "single_elim", "gauntlet", "bestOf"]

    options: Optional[BracketTypeOptions] = None


class BreakpointsGenerator(BaseModel):
    identifier: Optional[Literal["noop"]] = None


class BreakpointsInput(BaseModel):
    bracket: Optional[str] = None
    """The bracket ID"""

    roster: Optional[str] = None
    """The roster ID"""

    standing: Optional[int] = None


class BreakpointsRoles(BaseModel):
    creator: List[Role]

    owner: List[Role]


class Breakpoints(BaseModel):
    id: str
    """The breakpoint's ID"""

    generator: BreakpointsGenerator

    input: List[BreakpointsInput]

    name: str

    position: int

    roles: BreakpointsRoles

    scores: Dict[str, int]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    standings: Optional["Standings"] = None


class MatchTypeOptions(BaseModel):
    best_of: str


class MatchType(BaseModel):
    identifier: Literal["bestOf", "single_elim"]

    options: Optional[MatchTypeOptions] = None


class HighlanderTournament(BaseModel):
    id: str
    """The tournament Id

    It is a
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    """

    brackets: Dict[str, Brackets]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the bracket ID.
    """

    description: str
    """The tournament's name"""

    end_date: date = FieldInfo(alias="endDate")
    """The day the tournament ends/ended."""

    game_ids: List[str] = FieldInfo(alias="gameIds")
    """'Contains all the gameIds in this tournament.

    **Note:** The gameIds are in the format
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)'
    """

    league: str
    """The league ID"""

    league_id: str = FieldInfo(alias="leagueId")
    """The league ID"""

    league_reference: str = FieldInfo(alias="leagueReference")
    """The integer in the string represents the league ID."""

    live_matches: List[str] = FieldInfo(alias="liveMatches")
    """
    The array contains
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    Match IDs

    Despite the name of this property it is unreliable as for some tournaments this
    array will contain match IDs yet the matches are over.
    """

    platform_ids: List[str] = FieldInfo(alias="platformIds")
    """Contains all the platform IDs in for this tournaments.

    A platform ID is combination of the gameRealm and the gameId. The regex below
    describes the format.

    `^[A-Z]+\\dd+:\\dd+$`
    """

    published: Literal[True, False]
    """
    If the value is true then the league/tournament has concluded, otherwise it is
    ongoing.
    """

    queues: object

    roles: Roles

    rosters: Dict[str, Rosters]
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.

    Their values are objects but they don't contain anything useful about the
    roster.
    """

    start_date: date = FieldInfo(alias="startDate")
    """The day the tournament starts/started."""

    title: str
    """URL friendly version of the tournament name"""

    bracket_type: Optional[BracketType] = FieldInfo(alias="bracketType", default=None)

    breakpoints: Optional[Dict[str, Breakpoints]] = None
    """
    The keys to this object are
    [UUID version 4](https://en.wikipedia.org/wiki/Universally_unique_identifier)
    representing the roster ID.
    """

    match_type: Optional[MatchType] = FieldInfo(alias="matchType", default=None)

    rostering_strategy: Optional[RosteringStrategy] = FieldInfo(alias="rosteringStrategy", default=None)

    seeding_strategy: Optional[RosteringStrategy] = FieldInfo(alias="seedingStrategy", default=None)

    standings: Optional["Standings"] = None


from .standings import Standings
