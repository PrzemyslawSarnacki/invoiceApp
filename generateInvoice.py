import os
import datetime
import operationsMongo

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

# Program which generates Invoice from user input data
# choose english as language
os.environ["INVOICE_LANG"] = "pl"

provider = Provider('AS Lomza', 'Niewodowo 50', "18-421 Piątnica", bank_account='2600420569', bank_code='2010')
creator = Creator('')


def setClient(clientName, clientAddress, clientPostCode, clientAdditionalData):
    client = Client(clientName, clientAddress, clientPostCode, clientAdditionalData)
    invoice = Invoice(client, provider, creator, number=datetime.datetime.now().strftime("%d-%m-%y"))
    invoice.currency_locale = 'pl_PL.UTF-8'
    invoice.use_tax = True
    return invoice

def addItemToInvoice(invoice, dbItemCount, dbItemName, dbItemPrice):
    invoice.add_item(Item(dbItemCount, dbItemPrice, description=dbItemName, tax=23))

def createInvoice(invoice, totalAmount, paymentType, invoiceGenerationDate, invoicePaymentDate, invoiceSaleDate, invoiceNumber, discount, tax, invoiceType, taxAmount, warehouse, priceType, accountingNumber):
    pdf = SimpleInvoice(invoice)
    currentDate = datetime.datetime.now().strftime("%H.%M %d-%m-%y")
    pdf.gen("faktura " + str(currentDate) + ".pdf", generate_qr_code=True)
    invoiceCode = operationsMongo.Database("SP").getSingleLastData()["NR_KOD"] + 1
    warehouseDocumentCode = operationsMongo.Database("WZ").getSingleLastData()["NR_KOD"] + 1
    invoice.number = invoiceNumber
    # print(invoice.client.summary)
    operationsMongo.Database("SP").insertData({"NR_KOD":invoiceCode,"TYP_FS":invoiceType,"DATA":invoiceGenerationDate,"NUMER":accountingNumber,"MAGAZYN":int(warehouse),"PARTNER":invoice.client.summary,"WARTOSC":totalAmount,"UPUST":discount,"RODZ_PL":paymentType,"UWAGI_PL":'',"DATA_PL":invoicePaymentDate,"R_CEN":priceType,"MAGA":"PRAWDA","PODAT_WR": taxAmount,"DATA_SPRZ":invoiceSaleDate,"ZAT":"PRAWDA","NOP":1,"NR_DOK_MG":warehouseDocumentCode,"TYP_DOK_MG":"WZ","WAR_DOK_MG":689.0,"POMOCNICZE":"11","WALUTA":'PZL',"KURS":0.0,"WARTOSCWAL":'null',"TEKSTNUMER":'null'})
    operationsMongo.Database("WZ").insertData({"NR_KOD":warehouseDocumentCode,"DATA":invoiceGenerationDate,"NUMER":accountingNumber,"SKAD":invoiceNumber + " - " + invoiceGenerationDate,"DOKAD":invoice.client.summary,"WARTOSC":totalAmount,"R_CEN":priceType,"MAGAZYN":int(warehouse),"ZAT":"PRAWDA","NOP":1})
    
# 
# This is part for Purchase Invoice creation
# 

def setProvider(clientName, clientAddress, clientPostCode, clientAdditionalData):
    provider = Provider(clientName, clientAddress, clientPostCode, clientAdditionalData)
    client = Client('AS Lomza', 'Niewodowo 50', "18-421 Piątnica", bank_account='2600420569', bank_code='2010')
    invoice = Invoice(client, provider, creator, number=datetime.datetime.now().strftime("%d-%m-%y"))
    invoice.currency_locale = 'pl_PL.UTF-8'
    invoice.use_tax = True
    return invoice

def createPurchaseInvoice(invoice, totalAmount):
    pdf = SimpleInvoice(invoice)
    currentDate = datetime.datetime.now().strftime("%H.%M %d-%m-%y")
    currentDateDbFormat = datetime.datetime.now().strftime("%d.%m.%Y")
    pdf.gen("faktura " + str(currentDate) + ".pdf", generate_qr_code=True)
    invoiceCode = operationsMongo.Database("KU").getSingleLastData()["NR_KOD"] + 1
    invoiceCode = operationsMongo.Database("KU").getSingleLastData()["NR_KOD"] + 1
    print(invoice.client.summary)
    operationsMongo.Database("KU").insertData({"NR_KOD":invoiceCode,"TYP_FS":"H","DATA":currentDateDbFormat,"NUMER":89,"MAGAZYN":1,"PARTNER":invoice.client.summary,"WARTOSC":totalAmount,"UPUST":0.0,"RODZ_PL":"G","UWAGI_PL":'',"DATA_PL":'',"R_CEN":"H","MAGA":"PRAWDA","PODAT_WR":210.98,"DATA_SPRZ":currentDateDbFormat,"ZAT":"PRAWDA","NOP":1,"NR_DOK_MG":478.0,"TYP_DOK_MG":"WZ","WAR_DOK_MG":689.0,"POMOCNICZE":"11","WALUTA":'null',"KURS":0.0,"WARTOSCWAL":'null',"TEKSTNUMER":'null'})
