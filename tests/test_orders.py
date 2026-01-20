import pytest


@pytest.mark.asyncio
async def test_add_product_to_order(client):
    customer = await client.post(
        "/customers/",
        json={"name": "Alex"},
    )

    category = await client.post(
        "/categories/",
        json={"name": "Food"},
    )

    product = await client.post(
        "/products/",
        json={
            "name": "Apple",
            "quantity": 5,
            "price": 10,
            "category_id": category.json()["id"],
        },
    )

    order = await client.post(
        "/orders/",
        json={"customer_id": customer.json()["id"]},
    )

    response = await client.post(
        f"/orders/{order.json()['id']}/items",
        params={"product_id": product.json()["id"], "quantity": 2},
    )

    assert response.status_code == 200
