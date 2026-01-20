from fastapi import FastAPI

from Category.router import router as category_router
from Customer.router import router as customer_router
from Order.router import router as order_router
from Product.router import router as product_router

app = FastAPI(
    title="TZAitiGuru",
    description="Test task: FastAPI + Async SQLAlchemy",
    version="1.0.0",
)


@app.on_event("startup")
async def on_startup():
    """
    Startup hook.
    Схема БД управляется Alembic, здесь ничего не создаём.
    """
    pass


app.include_router(category_router)
app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)


@app.get("/", include_in_schema=False)
async def root():
    return {"status": "ok"}
