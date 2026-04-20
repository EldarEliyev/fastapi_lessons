from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional


app = FastAPI()

class Book(BaseModel):
    name: str 
    author: str 
    description: Optional[str] = None 
    price: float 
    page_count: int 
    tax: Optional[float] = None 


@app.post("/books/")
async def create_book(book: Book):
    book_dict = book.dict()
    if book.tax:
        price_with_tax = book.price + book.tax 
        book_dict.update({"price_with_tax":  price_with_tax})

    return book_dict


@app.put("/books/{book_id}")
async def update_book(book_id: int,  book: Book,  q: Optional[str] = None):
    result = {"book_id": book_id,  **book.dict()}
    if q:
        result.update({"q": q})
    return result 

