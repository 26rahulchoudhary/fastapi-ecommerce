from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.crud.category import (
    create_category,
    get_categories,
    get_category_by_id,
    update_category,
    delete_category
)

router = APIRouter(
    prefix="/api/categories",
    tags=["Categories"]
)


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)


@router.get("/", response_model=list[CategoryResponse])
def fetch_categories(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    skip = (page - 1) * limit
    return get_categories(db, skip, limit)


@router.get("/{category_id}", response_model=CategoryResponse)
def fetch_category(category_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.put("/{category_id}", response_model=CategoryResponse)
def update_existing_category(
    category_id: int,
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    updated_category = update_category(db, category_id, category)

    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")

    return updated_category


@router.delete("/{category_id}")
def remove_category(category_id: int, db: Session = Depends(get_db)):
    deleted_category = delete_category(db, category_id)

    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted successfully"}