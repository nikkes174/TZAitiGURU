import pytest


@pytest.mark.asyncio
async def test_total_by_customers(client):
    response = await client.get("/orders/reports/total-by-customers")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_top_5_products(client):
    response = await client.get("/products/reports/top-5-last-month")
    assert response.status_code == 200
