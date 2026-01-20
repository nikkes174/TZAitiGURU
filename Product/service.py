from datetime import datetime, timedelta

from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from Category.models import CategoryModel
from Order.models import OrderItemModel, OrderModel
from Product.crud import ProductCRUD
from Product.models import ProductModel
from Product.schemas import ProductCreate, TopProductReport


class ProductService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud = ProductCRUD(session)

    async def create_product(self, data: ProductCreate):
        return await self.crud.create(
            name=data.name,
            quantity=data.quantity,
            price=data.price,
            category_id=data.category_id,
        )

    async def list_products(self):
        return await self.crud.list()

    async def top_5_last_month(self):
        last_month = datetime.utcnow() - timedelta(days=30)

        stmt = (
            select(
                ProductModel.name.label("product_name"),
                CategoryModel.name.label("category_level_1"),
                func.sum(OrderItemModel.quantity).label("total_quantity"),
            )
            .join(OrderItemModel, OrderItemModel.product_id == ProductModel.id)
            .join(OrderModel, OrderModel.id == OrderItemModel.order_id)
            .join(CategoryModel, CategoryModel.id == ProductModel.category_id)
            .where(OrderModel.created_at >= last_month)
            .group_by(ProductModel.name, CategoryModel.name)
            .order_by(desc("total_quantity"))
            .limit(5)
        )

        res = await self.session.execute(stmt)

        return [
            TopProductReport(
                product_name=row.product_name,
                category_level_1=row.category_level_1,
                total_quantity=row.total_quantity,
            )
            for row in res
        ]
