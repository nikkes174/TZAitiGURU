from sqlalchemy.ext.asyncio import AsyncSession

from Customer.crud import CustomerCRUD
from Customer.schemas import CustomerCreate


class CustomerService:
    def __init__(self, session: AsyncSession):
        self.crud = CustomerCRUD(session)

    async def create_customer(self, data: CustomerCreate):
        return await self.crud.create(
            name=data.name,
            address=data.address,
        )
