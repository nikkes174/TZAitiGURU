from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id: int


class OrderRead(BaseModel):
    id: int
    customer_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class OrderTotalByCustomer(BaseModel):
    customer_name: str
    total_sum: Decimal

    class Config:
        from_attributes = True
