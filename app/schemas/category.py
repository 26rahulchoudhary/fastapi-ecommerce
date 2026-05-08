from pydantic import BaseModel, Field


# Request Schema
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)


# Response Schema
class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True