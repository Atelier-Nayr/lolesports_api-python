# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from lolesports_api import LolesportsAPI, AsyncLolesportsAPI
from lolesports_api.types import GetEventDetailRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGetEventDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LolesportsAPI) -> None:
        get_event_detail = client.get_event_details.retrieve(
            id=0,
            hl="en-US",
        )
        assert_matches_type(GetEventDetailRetrieveResponse, get_event_detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LolesportsAPI) -> None:
        response = client.get_event_details.with_raw_response.retrieve(
            id=0,
            hl="en-US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        get_event_detail = response.parse()
        assert_matches_type(GetEventDetailRetrieveResponse, get_event_detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LolesportsAPI) -> None:
        with client.get_event_details.with_streaming_response.retrieve(
            id=0,
            hl="en-US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            get_event_detail = response.parse()
            assert_matches_type(GetEventDetailRetrieveResponse, get_event_detail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGetEventDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLolesportsAPI) -> None:
        get_event_detail = await async_client.get_event_details.retrieve(
            id=0,
            hl="en-US",
        )
        assert_matches_type(GetEventDetailRetrieveResponse, get_event_detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLolesportsAPI) -> None:
        response = await async_client.get_event_details.with_raw_response.retrieve(
            id=0,
            hl="en-US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        get_event_detail = await response.parse()
        assert_matches_type(GetEventDetailRetrieveResponse, get_event_detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLolesportsAPI) -> None:
        async with async_client.get_event_details.with_streaming_response.retrieve(
            id=0,
            hl="en-US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            get_event_detail = await response.parse()
            assert_matches_type(GetEventDetailRetrieveResponse, get_event_detail, path=["response"])

        assert cast(Any, response.is_closed) is True
