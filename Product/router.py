from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db
from Product.schemas import ProductCreate, ProductRead, TopProductReport
from Product.service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductRead)
async def create_product(
    data: ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    service = ProductService(db)
    return await service.create_product(data)


@router.get("/", response_model=list[ProductRead])
async def list_products(
    db: AsyncSession = Depends(get_db),
):
    service = ProductService(db)
    return await service.list_products()


@router.get(
    "/reports/top-5-last-month",
    response_model=list[TopProductReport],
)
async def top_5_products(
    db: AsyncSession = Depends(get_db),
):
    service = ProductService(db)
    return await service.top_5_last_month()
