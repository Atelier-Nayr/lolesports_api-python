# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from lolesports_api import LolesportsAPI, AsyncLolesportsAPI
from lolesports_api.types import TeamListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LolesportsAPI) -> None:
        team = client.teams.list(
            slug="slug",
            tournament="ecc2efdd-ddfa-11a9-906f-9e4aada37aa7",
        )
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LolesportsAPI) -> None:
        response = client.teams.with_raw_response.list(
            slug="slug",
            tournament="ecc2efdd-ddfa-11a9-906f-9e4aada37aa7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LolesportsAPI) -> None:
        with client.teams.with_streaming_response.list(
            slug="slug",
            tournament="ecc2efdd-ddfa-11a9-906f-9e4aada37aa7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(TeamListResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLolesportsAPI) -> None:
        team = await async_client.teams.list(
            slug="slug",
            tournament="ecc2efdd-ddfa-11a9-906f-9e4aada37aa7",
        )
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLolesportsAPI) -> None:
        response = await async_client.teams.with_raw_response.list(
            slug="slug",
            tournament="ecc2efdd-ddfa-11a9-906f-9e4aada37aa7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(TeamListResponse, team, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLolesportsAPI) -> None:
        async with async_client.teams.with_streaming_response.list(
            slug="slug",
            tournament="ecc2efdd-ddfa-11a9-906f-9e4aada37aa7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(TeamListResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True
