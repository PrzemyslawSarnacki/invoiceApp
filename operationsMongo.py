import pymongo
import re
from bson import ObjectId
import generateInvoice

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
        data = self.collection.find({"$text": {"$search": search_this}})
        return list(data)
    
    
    def searchByNIP(self, search_this, collection):
        data = self.collection.find({"$kod": {"$search": search_this}})
        return list(data)


    def sortAlphabetically(self, collection):
        data = self.collection.find().sort("NAZWA_I", pymongo.ASCENDING)
        return list(data)
        # for item in collection.find({"$text": {"$search": search_this}}).limit(10): 
        #     print(item)
        #     return(item.get("KOSZT")), (item.get("NAZWA"))


    def update_or_create(self, document_id, data):
        document = self.collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
        return document.acknowledged


    def getSingleData(self, document_id):
        data = self.collection.find_one({'_id': ObjectId(document_id)})
        return data
    
    
    def getSingleLastData(self):
        data = self.collection.find_one(sort=[('NR_KOD', pymongo.DESCENDING)])
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


    def removeMultipleData(self):
        document = self.collection.delete_many({})
        return document.acknowledged


    def subtractDataFromWarehouse(self, document_id, invoice, amountOfStuff=1):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        # print(document)
        itemName = document["NAZWA"]
        itemPrice = document["KOSZT"]
        ILOSC = float(document['ILOSC'])
        ILOSC -= amountOfStuff
        print(ILOSC)
        document = self.collection.update_one({'_id': ObjectId(document_id)},{'$set' : {'ILOSC': ILOSC}})
        # document = self.collection.find_one({'_id': ObjectId(document_id)})
        # print(document)
        itemAndCountMultiplied = generateInvoice.addItemToInvoice(invoice, amountOfStuff, itemName, itemPrice)
        # generateInvoice.addItemToInvoice(invoice, amountOfStuff, document['NAZWA'], 500)
        # generateInvoice.createInvoice(invoice)
        return document.acknowledged, itemAndCountMultiplied
    
    def addDataToInvoiceList(self, document_id, invoice, amountOfStuff=1):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        # print(document)
        itemName = document["NAZWA"]
        itemPrice = document["KOSZT"]
        ILOSC = float(document['ILOSC'])
        ILOSC -= amountOfStuff
        myclient = pymongo.MongoClient('mongodb://localhost:27017')
        myclient.mongotest.TEMPSP.insertData({"NR_KOD":649,"LP":1,"LEK": itemName,"NUMER":'null',"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":amountOfStuff*itemPrice,"KOD":"0099","JEST_VAT":"PRAWDA","PODAT":23.0,"UPUST":0.0})
        return True

    def clearTemporaryTableForInvoice(self):
        Database("TEMPSP").removeMultipleData()
        Database("TEMPSP").insertData({"NR_KOD":1,"LP":'',"LEK":"","NUMER":'',"CENA":'',"ILOSC":'',"WARTOSC":'',"KOD":"","JEST_VAT":"","PODAT":'',"UPUST":'',"PREVID":''})

    def clearTemporaryTableForPurchaseInvoice(self):
        Database("TEMPKU").removeMultipleData()
        Database("TEMPKU").insertData({"NR_KOD":1,"LP":'',"LEK":"","NUMER":'',"CENA":'',"ILOSC":'',"WARTOSC":'',"KOD":"","PODAT":'',"KONTO_KU":'',"UPUST":'',"JEST_VAT":""})
    # search_this = "Aceton"
    # dbprice, dbname = searchForItem(search_this)
    # print(dbname)
    # print(getMultipleData())

# p1 = Database(collectionName)
# print(p1.getMultipleData())
# Database("TEMPSP").insertData({"NR_KOD":'',"LP":'',"LEK":"","NUMER":'',"CENA":'',"ILOSC":'',"WARTOSC":'',"KOD":"","JEST_VAT":"","PODAT":'',"UPUST":''})


# print(Database("SP").getSingleLastData()['NR_KOD'])

# myclient = pymongo.MongoClient('mongodb://localhost:27017')
# myclient.mongotest.KONTRAH.create_index([('KOD', 'kod')])
# Database("KONTRAH").create_index([('Rejestr', 'text')])
Database("TEMPSP").clearTemporaryTableForInvoice()
Database("TEMPKU").clearTemporaryTableForPurchaseInvoice()