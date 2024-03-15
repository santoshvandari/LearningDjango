from typing import Union
from fastapi import FastAPI
from allrequests import getquotes, addquotes,deletequotes,updatequotes

app = FastAPI()


@app.get("/")
def quotes():
    return getquotes()

@app.post("/add/")
async def addquote(quotes: str, author: str):
    quotes= quotes.strip()
    author= author.strip()
    if len(quotes) == 0 or len(author) == 0:
        return {"error": "Quotes and Author are required"}
    return addquotes(quotes,author)

@app.delete("/delete/")
async def deletequote(id):
    id=id.strip()
    if id:
        return {"error":"ID Cannot be Empty"}
    return deletequotes(id)


@app.put("/update/")
async def updatequote(quote:str,author:str,id):
    id=id.strip()
    quotes= quotes.strip()
    author= author.strip()
    if len(quotes) == 0 or len(author) == 0 or len(id)==0:
        return {"error": "ID, Quotes and Author are required"}
    return updatequotes(quote,author,id)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}