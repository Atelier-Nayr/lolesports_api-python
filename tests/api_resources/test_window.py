# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from lolesports_api import LolesportsAPI, AsyncLolesportsAPI
from lolesports_api.types import WindowRetrieveResponse
from lolesports_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWindow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LolesportsAPI) -> None:
        window = client.window.retrieve(
            game_id=0,
        )
        assert_matches_type(WindowRetrieveResponse, window, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LolesportsAPI) -> None:
        window = client.window.retrieve(
            game_id=0,
            starting_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WindowRetrieveResponse, window, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LolesportsAPI) -> None:
        response = client.window.with_raw_response.retrieve(
            game_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        window = response.parse()
        assert_matches_type(WindowRetrieveResponse, window, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LolesportsAPI) -> None:
        with client.window.with_streaming_response.retrieve(
            game_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            window = response.parse()
            assert_matches_type(WindowRetrieveResponse, window, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWindow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLolesportsAPI) -> None:
        window = await async_client.window.retrieve(
            game_id=0,
        )
        assert_matches_type(WindowRetrieveResponse, window, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLolesportsAPI) -> None:
        window = await async_client.window.retrieve(
            game_id=0,
            starting_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(WindowRetrieveResponse, window, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLolesportsAPI) -> None:
        response = await async_client.window.with_raw_response.retrieve(
            game_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        window = await response.parse()
        assert_matches_type(WindowRetrieveResponse, window, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLolesportsAPI) -> None:
        async with async_client.window.with_streaming_response.retrieve(
            game_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            window = await response.parse()
            assert_matches_type(WindowRetrieveResponse, window, path=["response"])

        assert cast(Any, response.is_closed) is True
