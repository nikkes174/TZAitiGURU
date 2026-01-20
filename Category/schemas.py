from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    parent_id: int | None = None


class CategoryRead(BaseModel):
    id: int
    name: str
    parent_id: Optional[int]

    class Config:
        from_attributes = True


class CategoryChildrenCount(BaseModel):
    id: int
    name: str
    children_count: int

    class Config:
        from_attributes = True
