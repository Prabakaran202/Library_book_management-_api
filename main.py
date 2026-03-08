from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import List,Optional


#shemashe 

class Book(BaseModel):
    id : int 
    title : str = Field(min_length=4)
    author : str =Field(min_length=3)
    price : float = 299.99
    available: bool =True

#creat router
app = FastAPI()

db:List[dict] = [{
    "id":1,
    "title":"The Great Gatsby",
    "author":"F. Scott Fitzgerald",
    "price":10.99,
    "available":True


},{
    "id":2,
    "title":"To Kill a Mockingbird",
    "author":"Harper Lee",
    "price":8.99,
    "available":True
},
{    "id":3,
    "title":"1984",
    "author":"George Orwell",
    "price":9.99,
    "available":True
},{
    "id":4,
    "title":"Pride and Prejudice",
    "author":"Jane Austen",
    "price":7.99,
    "available":True
}
]

#creat endpoints:
@app.get("/")
def root():
    return {"msg":"Library API is running!"}
#book add post creat

@app.post("/books")
def new_book(books:Book):
    if books:
        db.append(books.model_dump())
        return {"message":"book added successfully"}
    else:
        raise HTTPException(status_code=400,detail="book not added")
    


#get all books

@app.get("/books")
def find_all_books():
    return db

#creat find single book


@app.get("/books/{id}")
def find_book_by_id(id:int):
    for book in db:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404,detail="book not found")

#creat put (modfiy ) books datas

@app.put("/books/{id}/title/{Title}/price/{price}")

def bookupdatas(id:int,Title:str,price:float):
    for book in db :
        if book["id"] == id :
            book["title"] = Title
            book["price"] = price
        return {"msg": "book was updatat","book":book}
    raise HTTPException (status_code = 400, detail="wrong input")

@app.delete("/books/{id}")
def delete_book(id:int):
    for book in db:
        if book["id"] == id:
            db.remove(book)
            return {"msg":"book was deleted", "book": book}
    raise HTTPException(status_code=404,detail="book not found")
