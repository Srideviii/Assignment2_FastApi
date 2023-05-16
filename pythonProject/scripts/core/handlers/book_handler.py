from schemas.models import Book
from scripts.core.db.mongodb import book_1


def get_book():
    return {"hi"}


def create_book(book: Book):
    book_1.insert_one(book.dict())
    return {"ok"}


def update_book(book_id: int, book: Book):
    book_1.update_one({'book_id': book_id}, {'$set': book.dict()})
    return {"message": "Book updated successfully"}


def delete_book(book_id: int):
    book_1.delete_one({'book_id': book_id})
    return {"message": "Book deleted successfully"}
