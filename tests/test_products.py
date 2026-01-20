import pytest


@pytest.mark.asyncio
async def test_create_product(client):
    category = await client.post(
        "/categories/",
        json={"name": "Books"},
    )

    response = await client.post(
        "/products/",
        json={
            "name": "Python Book",
            "quantity": 10,
            "price": 100,
            "category_id": category.json()["id"],
        },
    )

    assert response.status_code == 200
    assert response.json()["quantity"] == 10
