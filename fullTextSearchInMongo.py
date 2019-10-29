import pymongo
import re

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
        print(item.get("KOSZT"))
        return(item.get("KOSZT")), (item.get("NAZWA"))


search_this = "promocja"

dbprice, dbname = searchForItem(search_this)
print(dbname)