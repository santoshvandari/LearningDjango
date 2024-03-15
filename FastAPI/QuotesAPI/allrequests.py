from DB.db import db
import random

def getquotes():
    quotes= list(db.quotes.find())
    quote= quotes[random.randint(0,len(quotes)-1)]
    return {"quotes": quote["quotes"], "author": quote["author"]}

def addquotes(quotes: str, author: str):
    try:
        db.quotes.insert_one({'quotes': quotes,'author': author})
    except Exception as e:
        return {"error": str(e)}