# E-Commerce FastAPI Backend

A RESTful backend API built using FastAPI, PostgreSQL, and SQLAlchemy for managing categories and products.

---

# Features

- Category CRUD APIs
- Product CRUD APIs
- One-to-Many Relationship
- Server-side Pagination
- PostgreSQL Integration
- SQLAlchemy ORM
- Pydantic Validation
- Swagger API Documentation

---

# Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

---

# Project Structure

```bash
app/
│
├── crud/
├── models/
├── routes/
├── schemas/
│
├── config.py
├── database.py
└── main.py
```

---

# Database Design

## Categories Table

| Column | Type |
|---|---|
| id | Integer |
| name | String |

---

## Products Table

| Column | Type |
|---|---|
| id | Integer |
| name | String |
| description | String |
| price | Float |
| category_id | Foreign Key |

---

# Relationship

One Category → Multiple Products

Each product belongs to one category.

---

# Installation

## Clone Repository

```bash
git clone <repository_url>
cd fastapi_machine_test
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ecommerce_db
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Categories

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/categories/` | Create category |
| GET | `/api/categories/` | Get all categories |
| GET | `/api/categories/{id}` | Get category by ID |
| PUT | `/api/categories/{id}` | Update category |
| DELETE | `/api/categories/{id}` | Delete category |

---

## Products

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/products/` | Create product |
| GET | `/api/products/` | Get all products |
| GET | `/api/products/{id}` | Get product by ID |
| PUT | `/api/products/{id}` | Update product |
| DELETE | `/api/products/{id}` | Delete product |

---

# Pagination Example

```http
GET /api/products?page=1&limit=5
```

---

# Author

Rahul Choudhary