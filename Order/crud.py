from sqlalchemy.ext.asyncio import AsyncSession

from Order.models import OrderModel


class OrderCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, customer_id: int):
        order = OrderModel(customer_id=customer_id)
        self.session.add(order)
        await self.session.commit()
        await self.session.refresh(order)
        return order

    async def get(self, order_id: int):
        return await self.session.get(OrderModel, order_id)
