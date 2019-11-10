import os
import datetime

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

def createInvoice(invoice):
    pdf = SimpleInvoice(invoice)
    currentDate = datetime.datetime.now().strftime("%H.%M %d-%m-%y")
    pdf.gen("faktura " + str(currentDate) + ".pdf", generate_qr_code=True)

