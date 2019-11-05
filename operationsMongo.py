import pymongo
import re
from bson import ObjectId

# collectionName = "ASOR"

class Database:
    def __init__(self, collectionName):
        
        myclient = pymongo.MongoClient('mongodb://localhost:27017')
        
        database = myclient.mongotest
        # ASOR is the name of collection in mongotest database
        self.collection = database[collectionName]

#Search for item in certain collection 
# By using create_index you can search specified key 
# in collection(NAZWA in this case)
# collection.create_index([('NAZWA', 'text')])

    def searchForItem(self, search_this, collection):
        self.collection.find({"$text": {"$search": search_this}})
        for item in collection.find({"$text": {"$search": search_this}}).limit(1): 
            print(item)
            return(item.get("KOSZT")), (item.get("NAZWA"))


    def update_or_create(self, document_id, data):
        document = self.collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
        return document.acknowledged


    def getSingleData(self, document_id):
        data = self.collection.find_one({'_id': ObjectId(document_id)})
        return data


    def getMultipleData(self):
        data = self.collection.find()
        return list(data)


    def updateData(self, document_id, data):
        document = self.collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
        return document.acknowledged


    def insertData(self, data):
        document = self.collection.insert_one(data)
        return document.inserted_id


    def removeData(self, document_id):
        document = self.collection.delete_one({'_id': ObjectId(document_id)})
        return document.acknowledged

    # search_this = "Aceton"
    # dbprice, dbname = searchForItem(search_this)
    # print(dbname)
    # print(getMultipleData())

# p1 = Database(collectionName)
# print(p1.getMultipleData())