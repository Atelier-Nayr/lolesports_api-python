# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["LeagueListParams", "Query", "QueryID", "QuerySlug"]


class LeagueListParams(TypedDict, total=False):
    query: Required[Query]
    """'This endpoint requires either the id or the slug to be passed.

    If both are present then only the first one will be considered.

    _Due to a limitation in the OpenApi specification it is not possible to show the
    mutual exclusive nature that the query parameters in this endpoint require. The
    schema below is as close as a representation I could get in expressing the
    nature of the query parameters._

    Check the examples below to help better understand the query parameters needed.

    **Example 1**

    `https://api.lolesports.com/api/v1/leagues?id=3`

    This will return the details for **LEC**.

    **Example 2**

    `https://api.lolesports.com/api/v1/leagues?slug=worlds`

    This will return the details for **Worlds**

    **Example 3**

    `https://api.lolesports.com/api/v1/leagues?id=3&slug=worlds`

    In such a scenario where both query parameters are used only the first will be
    considered, hence it will only return the details for **LEC**.

    **Example 4**

    `https://api.lolesports.com/api/v1/leagues`

    This is not valid. At least one of the two query parameters (id or slug) is
    required.'
    """


class QueryID(TypedDict, total=False):
    id: Required[int]


class QuerySlug(TypedDict, total=False):
    slug: Required[str]


Query: TypeAlias = Union[QueryID, QuerySlug]
