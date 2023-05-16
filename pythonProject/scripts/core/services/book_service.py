from fastapi import APIRouter
from scripts.core.handlers.book_handler import *

app = APIRouter()


@app.get("/")
def fun():
    return get_book()


@app.post("/books/book_id")
def fun(book: Book):
    return create_book(book)


@app.put("/book/{book_id}")
def upd(book_id: int, book: Book):
    return update_book(book_id, book)


@app.delete("/books/{book_id}")
def de(book_id: int):
    return delete_book(book_id)
