from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.category import Category
from app.schemas.product import ProductCreate


# create product
def create_product(db: Session, product: ProductCreate):

    category = db.query(Category).filter(
        Category.id == product.category_id
    ).first()

    if not category:
        return None

    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


# Get All Products with Pagination
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()


# Get Product By ID
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# Update Product
def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product_by_id(db, product_id)

    if not db_product:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.category_id = product.category_id

    db.commit()
    db.refresh(db_product)

    return db_product


# Delete Product
def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)

    if not db_product:
        return None

    db.delete(db_product)
    db.commit()

    return db_product