import pytest


@pytest.mark.asyncio
async def test_category_tree(client):
    parent = await client.post(
        "/categories/",
        json={"name": "Electronics"},
    )
    parent_id = parent.json()["id"]

    child = await client.post(
        "/categories/",
        json={"name": "Phones", "parent_id": parent_id},
    )

    assert child.status_code == 200

    report = await client.get("/categories/reports/children-count")
    assert report.status_code == 200
