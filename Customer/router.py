from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from Customer.schemas import CustomerCreate, CustomerRead
from Customer.service import CustomerService
from db import get_db

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerRead)
async def create_customer(
    data: CustomerCreate,
    db: AsyncSession = Depends(get_db),
):
    service = CustomerService(db)
    return await service.create_customer(data)
