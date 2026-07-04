from fastapi import FastAPI

from app.api import books, categories
from app.db.db import create_tables


app = FastAPI(title="Books API", version="1.0.0")

app.include_router(categories.router)
app.include_router(books.router)


@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/health")
def health():
    return {"status": "ok"}
