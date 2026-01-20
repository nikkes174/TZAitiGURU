import asyncio

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from Category.router import router as category_router
from Customer.router import router as customer_router
from db import Base, get_db
from Order.router import router as order_router
from Product.router import router as product_router

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_test.db"


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture
async def session(engine):
    async_session = async_sessionmaker(
        engine,
        expire_on_commit=False,
        autoflush=False,
    )
    async with async_session() as session:
        yield session


@pytest.fixture
async def app(session):
    app = FastAPI()

    async def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db

    app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(customer_router)
    app.include_router(order_router)

    yield app


@pytest.fixture
async def client(app):
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        yield client
