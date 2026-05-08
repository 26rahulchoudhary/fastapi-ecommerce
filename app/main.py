from fastapi import FastAPI

from app.database import engine, Base

# Import models
from app.models.category import Category
from app.models.product import Product

# Import routers
from app.routes.category import router as category_router
from app.routes.product import router as product_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(category_router)
app.include_router(product_router)


@app.get("/")
def root():
    return {"message": "FastAPI Machine Test Running"}