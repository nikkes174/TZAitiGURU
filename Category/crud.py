from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import CategoryModel


class CategoryCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, name: str, parent_id: int | None = None):
        category = CategoryModel(
            name=name,
            parent_id=parent_id,
        )
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def list(self):
        stmt = select(CategoryModel)
        res = await self.session.execute(stmt)
        return res.scalars().all()
