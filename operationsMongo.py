import pymongo
import re
from bson import ObjectId


#Search for item in certain collection 

myclient = pymongo.MongoClient('mongodb://localhost:27017')
database = myclient.mongotest
# ASOR is the name of collection in mongotest database
collection = database.ASOR

# By using create_index you can search specified key 
# in collection(NAZWA in this case)
# collection.create_index([('NAZWA', 'text')])

 
def searchForItem(search_this):
    collection.find({"$text": {"$search": search_this}})
    for item in collection.find({"$text": {"$search": search_this}}).limit(1): 
        print(item)
        return(item.get("KOSZT")), (item.get("NAZWA"))


def update_or_create(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def getSingleData(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data


def getMultipleData():
    data = collection.find().limit(10)
    return list(data)


def updateData(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged


def insertData(data):
    document = collection.insert_one(data)
    return document.inserted_id


def removeData(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged

search_this = "Aceton"
dbprice, dbname = searchForItem(search_this)
# print(dbname)
# print(getMultipleData())
