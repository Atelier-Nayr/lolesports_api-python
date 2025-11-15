# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from lolesports_api import LolesportsAPI, AsyncLolesportsAPI
from lolesports_api.types import NavItemListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNavItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LolesportsAPI) -> None:
        nav_item = client.nav_items.list()
        assert_matches_type(NavItemListResponse, nav_item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LolesportsAPI) -> None:
        response = client.nav_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nav_item = response.parse()
        assert_matches_type(NavItemListResponse, nav_item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LolesportsAPI) -> None:
        with client.nav_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nav_item = response.parse()
            assert_matches_type(NavItemListResponse, nav_item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNavItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLolesportsAPI) -> None:
        nav_item = await async_client.nav_items.list()
        assert_matches_type(NavItemListResponse, nav_item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLolesportsAPI) -> None:
        response = await async_client.nav_items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nav_item = await response.parse()
        assert_matches_type(NavItemListResponse, nav_item, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLolesportsAPI) -> None:
        async with async_client.nav_items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nav_item = await response.parse()
            assert_matches_type(NavItemListResponse, nav_item, path=["response"])

        assert cast(Any, response.is_closed) is True
