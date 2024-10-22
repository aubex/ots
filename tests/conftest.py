from contextlib import asynccontextmanager

import pytest
from httpx import AsyncClient
from starlette.applications import Starlette

from src.ots.main import app


@asynccontextmanager
async def lifespan(app: Starlette):
    print("starting up")
    yield
    print("shutting down")


@pytest.fixture
async def client():
    async with lifespan(app):
        async with AsyncClient(app=app, base_url="http://testserver") as aclient:
            yield aclient
