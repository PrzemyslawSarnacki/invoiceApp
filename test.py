import generateInvoice

class Database:
    def __init__(self, collectionName):
        myclient = pymongo.MongoClient('mongodb://localhost:27017')
        self.database = myclient.mongotest
        # ASOR is the name of collection in mongotest database
        self.collection = database[collectionName]


print(Database.database.list_collection_names())
