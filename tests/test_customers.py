import pytest


@pytest.mark.asyncio
async def test_create_customer(client):
    response = await client.post(
        "/customers/",
        json={"name": "Ivan", "address": "Moscow"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ivan"
