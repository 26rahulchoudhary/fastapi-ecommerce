from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


# Create Category
def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


# Get All Categories with Pagination
def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()


# Get Category By ID
def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


# Update Category
def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = get_category_by_id(db, category_id)

    if not db_category:
        return None

    db_category.name = category.name

    db.commit()
    db.refresh(db_category)

    return db_category


# Delete Category
def delete_category(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)

    if not db_category:
        return None

    db.delete(db_category)
    db.commit()

    return db_category