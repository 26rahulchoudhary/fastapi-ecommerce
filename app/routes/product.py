from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductWithCategoryResponse
)

from app.crud.product import (
    create_product,
    get_products,
    get_product_by_id,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):

    created_product = create_product(db, product)

    if not created_product:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return created_product


@router.get("/", response_model=list[ProductResponse])
def fetch_products(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * limit
    return get_products(db, skip, limit)


@router.get("/{product_id}", response_model=ProductWithCategoryResponse)
def fetch_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_existing_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    updated_product = update_product(db, product_id, product)

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product


@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = delete_product(db, product_id)

    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}