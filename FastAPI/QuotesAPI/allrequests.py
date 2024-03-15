from DB.db import db
import random

def getquotes():
    quotes= list(db.quotes.find())
    quote= quotes[random.randint(0,len(quotes)-1)]
    return {"quotes": quote["quotes"], "author": quote["author"]}

def addquotes(quotes: str, author: str):
    try:
        db.quotes.insert_one({'quotes': quotes,'author': author})
        return {"success":"Quotes Added Successfully"}
    except Exception as e:
        return {"error": str(e)}
    
def updatequotes(quotes:str,author:str,id):
    try:
        pass
    except Exception as ex:
        pass
    pass

def deletequotes(id):
    try:
        pass
    except Exception as e:
        pass
    pass