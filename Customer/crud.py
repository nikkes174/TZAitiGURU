from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import CustomerModel


class CustomerCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, name: str, address: str | None):
        customer = CustomerModel(
            name=name,
            address=address,
        )
        self.session.add(customer)
        await self.session.commit()
        await self.session.refresh(customer)
        return customer

    async def list(self):
        stmt = select(CustomerModel)
        res = await self.session.execute(stmt)
        return res.scalars().all()
