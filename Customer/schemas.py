from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    address: str | None = None


class CustomerRead(BaseModel):
    id: int
    name: str
    address: str | None

    class Config:
        from_attributes = True
