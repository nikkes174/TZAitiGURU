from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from Order.schemas import OrderCreate, OrderRead, OrderTotalByCustomer
from Order.service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderRead)
async def create_order(
    data: OrderCreate,
    db: AsyncSession = Depends(get_db),
):
    service = OrderService(db)
    return await service.create_order(data.customer_id)


@router.get("/{order_id}", response_model=OrderRead)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = OrderService(db)
    return await service.get_order(order_id)


@router.post("/{order_id}/items")
async def add_product_to_order(
    order_id: int,
    product_id: int = Query(...),
    quantity: int = Query(..., gt=0),
    db: AsyncSession = Depends(get_db),
):
    service = OrderService(db)
    return await service.add_product(
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
    )


@router.get(
    "/reports/total-by-customers",
    response_model=list[OrderTotalByCustomer],
)
async def total_by_customers(
    db: AsyncSession = Depends(get_db),
):
    service = OrderService(db)
    return await service.total_sum_by_customers()
