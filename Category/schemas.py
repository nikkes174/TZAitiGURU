from __future__ import annotations

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    parent_id: int | None = None


class CategoryRead(BaseModel):
    id: int
    name: str
    parent_id: int | None

    class Config:
        from_attributes = True


class CategoryChildrenCount(BaseModel):
    id: int
    name: str
    children_count: int

    class Config:
        from_attributes = True
