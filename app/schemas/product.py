from pydantic import BaseModel, Field
from app.schemas.category import CategoryResponse
from typing import Optional


# Request Schema
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    category_id: int


# Response Schema
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

    class Config:
        from_attributes = True


# Nested Response Schema
class ProductWithCategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    category: CategoryResponse

    class Config:
        from_attributes = True