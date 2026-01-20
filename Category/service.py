from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from Category.crud import CategoryCRUD
from Category.models import CategoryModel
from Category.schemas import CategoryChildrenCount, CategoryCreate


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud = CategoryCRUD(session)

    async def create_category(self, data: CategoryCreate):
        return await self.crud.create(
            name=data.name,
            parent_id=data.parent_id,
        )

    async def children_count_level_1(self):
        parent = aliased(CategoryModel)
        child = aliased(CategoryModel)

        stmt = (
            select(
                parent.id.label("id"),
                parent.name.label("name"),
                func.count(child.id).label("children_count"),
            )
            .select_from(parent)
            .outerjoin(child, child.parent_id == parent.id)
            .group_by(parent.id, parent.name)
        )

        res = await self.session.execute(stmt)

        return [
            CategoryChildrenCount(
                id=row.id,
                name=row.name,
                children_count=row.children_count,
            )
            for row in res
        ]
