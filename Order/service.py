from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from Customer.models import CustomerModel
from Order.crud import OrderCRUD
from Order.models import OrderItemModel, OrderModel
from Order.schemas import OrderTotalByCustomer
from Product.models import ProductModel


class OrderService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.crud = OrderCRUD(session)

    async def create_order(self, customer_id: int):
        return await self.crud.create(customer_id)

    async def get_order(self, order_id: int):
        order = await self.crud.get(order_id)
        if not order:
            raise HTTPException(404, "Заказ не найден")
        return order

    async def add_product(
        self,
        order_id: int,
        product_id: int,
        quantity: int,
    ):
        product = await self.session.get(ProductModel, product_id)

        if not product or product.quantity < quantity:
            raise HTTPException(400, "Товара нет в наличии")

        item = await self.session.get(
            OrderItemModel,
            (order_id, product_id),
        )

        if item:
            item.quantity += quantity
        else:
            item = OrderItemModel(
                order_id=order_id,
                product_id=product_id,
                quantity=quantity,
                price=product.price,
            )
            self.session.add(item)

        product.quantity -= quantity
        await self.session.commit()

    async def total_sum_by_customers(self):
        stmt = (
            select(
                CustomerModel.name.label("customer_name"),
                func.sum(OrderItemModel.quantity * ProductModel.price).label(
                    "total_sum"
                ),
            )
            .join(OrderModel, OrderModel.customer_id == CustomerModel.id)
            .join(OrderItemModel, OrderItemModel.order_id == OrderModel.id)
            .join(ProductModel, ProductModel.id == OrderItemModel.product_id)
            .group_by(CustomerModel.name)
        )

        res = await self.session.execute(stmt)

        return [
            OrderTotalByCustomer(
                customer_name=row.customer_name,
                total_sum=row.total_sum,
            )
            for row in res
        ]
