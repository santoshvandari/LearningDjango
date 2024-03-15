from typing import Union
from fastapi import FastAPI
from allrequests import getquotes, addquotes

app = FastAPI()


@app.get("/")
def quotes():
    return getquotes()

@app.post("/add/")
async def addquotes(quotes: str, author: str):
    quotes= quotes.strip()
    author= author.strip()
    if len(quotes) == 0 or len(author) == 0:
        return {"error": "Quotes and Author are required"}

    return {"quotes": quotes, "author": author}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}