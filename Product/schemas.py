from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: float
    category_id: int


class ProductRead(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
    category_id: int

    class Config:
        from_attributes = True


class TopProductReport(BaseModel):
    product_name: str
    category_level_1: str
    total_quantity: int

    class Config:
        from_attributes = True
