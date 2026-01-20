from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Product.models import ProductModel


class ProductCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        name: str,
        quantity: int,
        price: float,
        category_id: int,
    ):
        product = ProductModel(
            name=name,
            quantity=quantity,
            price=price,
            category_id=category_id,
        )
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def list(self):
        stmt = select(ProductModel)
        res = await self.session.execute(stmt)
        return res.scalars().all()

    async def get(self, product_id: int):
        return await self.session.get(ProductModel, product_id)
