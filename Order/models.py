from sqlalchemy import DateTime, ForeignKey, Numeric
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from db import Base


class OrderModel(AsyncAttrs, Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    customer = relationship(
        "CustomerModel",
        back_populates="orders",
        lazy="selectin",
    )

    items = relationship(
        "OrderItemModel",
        back_populates="order",
        lazy="selectin",
    )


class OrderItemModel(AsyncAttrs, Base):
    __tablename__ = "order_items"

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
        primary_key=True,
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        primary_key=True,
    )
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)

    order = relationship("OrderModel", back_populates="items")
