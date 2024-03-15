from pymongo import MongoClient

# MONGO_URI='<Insert your MongoDB URI>'
# password: YFGnultHcQBMoqan
# username : santoshvandariquotes
# connectionuri = mongodb+srv://<username>:<password>@quotescollections.sqnxbjd.mongodb.net/
MONGO_URI="mongodb+srv://santoshvandariquotes:YFGnultHcQBMoqan@quotescollections.sqnxbjd.mongodb.net/"

# connect to the database pymongo 
try:
    client = MongoClient(MONGO_URI)
    db = client.get_database('quotes')
    # db.quotes.insert_one({'quotes': 'Santosh Bhandari is Still Testing','author':"Santosh Bhandari"})
    # 
    # fetch the random quotes from the mongodb database 
    quotes = db.quotes.find_one()
    # quotes = db.quotes.find({})

    # for quote in quotes:
    #     print(quote)
    # print(quotes)
    print('Connected to the database')
except Exception as e:
    print(f'Error connecting to the database: {e}')
    client = None
    exit(1)
