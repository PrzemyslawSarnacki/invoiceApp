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

    def searchForItem(self, search_this, collection, searchedKey):
        # data = self.collection.find({"$text": {"$searcth": "/" + search_this + "/"}})
        data = self.collection.find({searchedKey: {"$regex":  search_this }})
        return list(data)
    
    
    def searchByNumer(self, search_this, collection, searchedKey):
        data = self.collection.find({searchedKey: search_this})
        return list(data)


    def sortAscending(self, collection, collumnToSort):
        data = self.collection.find().sort(collumnToSort, pymongo.ASCENDING)
        return list(data)

    def sortDescending(self, collection, collumnToSort):
        data = self.collection.find().sort(collumnToSort, pymongo.DESCENDING)
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

    def getSingleDataByKey(self, certainKey, value):
        data = self.collection.find({}, {certainKey : 0, value : 1})
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


    def subtractDataFromWarehouse(self, document_id, invoice, listPosition, amountOfStuff=1, tax=23.0, discount=0, vatCondition="PRAWDA", invoiceGenerationDate="", invoiceNumber=""):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        # print(document)
        itemName = document["NAZWA"]
        itemPrice = float(document["KOSZT"])
        itemCode = document["KOD"]
        invoiceCode = Database("SP").getSingleLastData()["NR_KOD"] + 1
        if discount != 0:
            itemPrice = itemPrice * ((100-discount)/100)
        if vatCondition == "FAŁSZ":
            tax = 0
        ILOSC = float(document['ILOSC'])
        ILOSC -= amountOfStuff
        print(ILOSC)
        document = self.collection.update_one({'_id': ObjectId(document_id)},{'$set' : {'ILOSC': ILOSC}})
        generateInvoice.addItemToInvoice(invoice, amountOfStuff, itemName, itemPrice)
        warehouseDocumentCode = Database("WZ").getSingleLastData()["NUMER"] + 1

        Database("SPZAW").insertData({"NR_KOD": invoiceCode,"LP":listPosition,"LEK": itemName,"NUMER":'null',"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":float(amountOfStuff)*float(itemPrice),"KOD":itemCode,"JEST_VAT":vatCondition,"PODAT":tax,"UPUST":discount})

        Database("KARTA1").insertData({"STR_DZIENN":'',"DATA":invoiceGenerationDate,"NR_DOWODU":"WZ_" + warehouseDocumentCode + "/1","TRESC":invoiceNumber + " - " + invoice.client.summary,"CENA_JEDN":itemPrice,"IL_PRZYCH":0.0,"IL_ROZCH":amountOfStuff,"IL_ZAPAS":ILOSC,"WR_PRZYCH":0.0,"WR_ROZCH":float(amountOfStuff)*float(itemPrice),"WR_ZAPAS":float(ILOSC)*float(itemPrice),"KOD":itemCode,"ZNACZNIK":''})
        return document.acknowledged

    def subtractDataFromWarehouseWZ(self, document_id, invoice, listPosition, amountOfStuff=1):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        itemName = document["NAZWA"]
        itemPrice = float(document["KOSZT"])
        itemCode = document["KOD"]
        invoiceCode = Database("WZ").getSingleLastData()["NR_KOD"] + 1
        invoiceNumber = Database("WZ").getSingleLastData()["NUMER"] + 1
        ILOSC = float(document['ILOSC'])
        ILOSC -= amountOfStuff
        document = self.collection.update_one({'_id': ObjectId(document_id)},{'$set' : {'ILOSC': ILOSC}})
        # generateInvoice.addItemToInvoice(invoice, amountOfStuff, itemName, itemPrice)
        Database("WZZAW").insertData({"NR_KOD": invoiceCode,"LP":listPosition,"LEK": itemName,"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":float(amountOfStuff)*float(itemPrice),"KOD":itemCode})
        Database("KARTA1").insertData({"STR_DZIENN":'',"DATA":'',"NR_DOWODU":"WZ_" + invoiceNumber + "/1","TRESC":"NUMER - " + invoice.client.summary,"CENA_JEDN":itemPrice,"IL_PRZYCH":0.0,"IL_ROZCH":amountOfStuff,"IL_ZAPAS":ILOSC,"WR_PRZYCH":0.0,"WR_ROZCH":float(amountOfStuff)*float(itemPrice),"WR_ZAPAS":float(ILOSC)*float(itemPrice),"KOD":itemCode,"ZNACZNIK":''})
        return document.acknowledged
    
    def subtractDataFromWarehousePZ(self, document_id, invoice, listPosition, amountOfStuff=1):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        itemName = document["NAZWA"]
        itemPrice = float(document["KOSZT"])
        itemCode = document["KOD"]
        invoiceCode = Database("PZ").getSingleLastData()["NR_KOD"] + 1
        ILOSC = float(document['ILOSC'])
        ILOSC -= amountOfStuff
        document = self.collection.update_one({'_id': ObjectId(document_id)},{'$set' : {'ILOSC': ILOSC}})
        # generateInvoice.addItemToInvoice(invoice, amountOfStuff, itemName, itemPrice)
        Database("PZZAW").insertData({"NR_KOD": invoiceCode,"LP":listPosition,"LEK": itemName,"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":float(amountOfStuff)*float(itemPrice),"KOD":itemCode})
        return document.acknowledged
    
    def addDataToWarehouse(self, document_id, listPosition, amountOfStuff=1):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        itemName = document["NAZWA"]
        itemPrice = float(document["KOSZT"])
        itemCode = document["KOD"]
        invoiceCode = Database("KU").getSingleLastData()["NR_KOD"] + 1
        ILOSC = float(document['ILOSC'])
        ILOSC += amountOfStuff
        document = self.collection.update_one({'_id': ObjectId(document_id)},{'$set' : {'ILOSC': ILOSC}})
        # generateInvoice.addItemToInvoice(invoice, amountOfStuff, itemName, itemPrice)
        Database("KUZAW").insertData({"NR_KOD": invoiceCode,"LP":listPosition,"LEK": itemName,"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":float(amountOfStuff)*float(itemPrice),"KOD":itemCode})
        return document.acknowledged
    
    def createWZ(self, totalAmount, wzGenerationDate, wzNumber, wzType, warehouse, priceType,destination="super"):
        wzCode = Database("WZ").getSingleLastData()["NR_KOD"] + 1
        # yearlyNumber = int((((operationsMongo.Database("WZ").getSingleLastData()["NUMER"]).split("/"))[0]).strip("H"))
        
        if wzType == "H":
            yearlyNumber = (Database("WZ").getSingleDataByKey("NR_KOD", wzCode))["NUMER"]
            # yearlyNumber = 1 if wzGenerationDate.split(".")[1] == '01'else (Database("WZ").getSingleLastData()["NUMER"] + 1)
        else:
            yearlyNumber = 1

        sourceString = wzType + yearlyNumber + "/1 - " + wzGenerationDate
        Database("WZ").insertData({"NR_KOD":wzCode,"DATA":wzGenerationDate,"NUMER":yearlyNumber,"SKAD":sourceString,"DOKAD":destination,"WARTOSC":totalAmount,"R_CEN":priceType,"MAGAZYN":int(warehouse),"ZAT":"PRAWDA","NOP":1})
    
    def createPurchaseInvoice(self, totalAmount, clientName, invoiceGenerationDate, invoiceInflowDate, discount, invoicePaymentDate, invoiceNumber, invoiceType, warehouse, priceType, paymentType):
        invoiceCode = Database("KU").getSingleLastData()["NR_KOD"] + 1
        # yearlyNumber = int((((operationsMongo.Database("WZ").getSingleLastData()["NUMER"]).split("/"))[0]).strip("H"))
        
        if invoiceType == "H":
            yearlyNumber = (Database("KU").getSingleDataByKey("NR_KOD", invoiceCode))["NUMER"]
            # yearlyNumber = 1 if wzGenerationDate.split(".")[1] == '01'else (Database("WZ").getSingleLastData()["NUMER"] + 1)
        else:
            yearlyNumber = 1

        Database("KU").insertData({"NR_KOD":invoiceCode,"DATA":invoiceGenerationDate,"DATA_WPLYW":invoiceInflowDate,"NR_KSIEG":yearlyNumber,"NUMER":yearlyNumber,"PARTNER":clientName,"WARTOSC":totalAmount,"UPUST_PR":discount,"N_VAT":"","RODZ_PL":paymentType,"DATA_PL":invoicePaymentDate,"R_CEN":priceType,"MAGA":"PRAWDA","MAGAZYN":warehouse,"ZAT":"PRAWDA","UZGOD":"PRAWDA","NOP":1,"WALUTA":"PZL","KURS":0.0,"WARTOSCWAL":0.0,"WARTOSCTRA":0.0,"WARTOSCCLO":0.0,"WARTOSCPIM":0.0,"OPIS":'null'})


    def addDataToInvoiceList(self, document_id, invoice, amountOfStuff, tempList):
        document = self.collection.find_one({'_id': ObjectId(document_id)})
        # print(document)
        itemName = document["NAZWA"]
        itemPrice = document["KOSZT"]
        itemCode = document["NR_KOD"]
        ILOSC = float(document['ILOSC'])
        ILOSC -= amountOfStuff
        if tempList == "TEMPSP":
            Database("TEMPSP").insertData({"NR_KOD":649,"LP":1,"LEK": itemName,"NUMER":'null',"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":amountOfStuff*itemPrice,"KOD":itemCode,"JEST_VAT":"PRAWDA","PODAT":23.0,"UPUST":0.0})
        elif tempList == "TEMPKU":
            Database("TEMPKU").insertData({"NR_KOD":1,"LP":1,"LEK":itemName,"NUMER":'null',"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":amountOfStuff,"KOD":itemCode,"PODAT":23.0,"KONTO_KU":'',"UPUST":0.0,"JEST_VAT":"PRAWDA","PREVID":''})
        return True

    def clearTemporaryTableForInvoice(self):
        Database("TEMPSP").removeMultipleData()
        Database("TEMPSP").insertData({"NR_KOD":1,"LP":'',"LEK":"","NUMER":'',"CENA":'',"ILOSC":'',"WARTOSC":'',"KOD":"","JEST_VAT":"","PODAT":'',"UPUST":'',"PREVID":''})

    def clearTemporaryTableForPurchaseInvoice(self):
        Database("TEMPKU").removeMultipleData()
        Database("TEMPKU").insertData({"NR_KOD":1,"LP":'',"LEK":"","NUMER":'',"CENA":'',"ILOSC":'',"WARTOSC":'',"KOD":"","PODAT":'',"KONTO_KU":'',"UPUST":'',"JEST_VAT":"","PREVID":''})
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
# print(list(myclient.mongotest.KONTRAH.find({},{'REJESTR': '731'})))
# Database("KONTRAH").create_index([('Rejestr', 'text')])
Database("TEMPSP").clearTemporaryTableForInvoice()
Database("TEMPKU").clearTemporaryTableForPurchaseInvoice()