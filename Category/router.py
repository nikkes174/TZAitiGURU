from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Category.schemas import (
    CategoryChildrenCount,
    CategoryCreate,
    CategoryRead,
)
from Category.service import CategoryService
from db import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryRead)
async def create_category(
    data: CategoryCreate,
    db: AsyncSession = Depends(get_db),
):
    service = CategoryService(db)
    return await service.create_category(data)


@router.get(
    "/reports/children-count",
    response_model=list[CategoryChildrenCount],
)
async def children_count(db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    return await service.children_count_level_1()
