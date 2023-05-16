from fastapi import FastAPI
from scripts.core.services.book_service import app as book

app = FastAPI()
app.include_router(book)

import uvicorn

if __name__ == "main__":
    uvicorn.run("main:app")
