import os
import datetime
import fullTextSearchInMongo 

from tempfile import NamedTemporaryFile

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

# Program which generates Invoice from user input data
# choose english as language
os.environ["INVOICE_LANG"] = "pl"

client = Client('AS Lomza', 'Niewodowo 50', "18-421 Piątnica", 'AS Lomza')
provider = Provider('AS Lomza', 'Niewodowo 50', "18-421 Piątnica", bank_account='2600420569', bank_code='2010')
creator = Creator('')

invoice = Invoice(client, provider, creator, number=datetime.datetime.now().strftime("%d-%m-%y"))
invoice.currency_locale = 'pl_PL.UTF-8'
invoice.use_tax = True
invoice.add_item(Item(32, 60, description="Item 1", tax=23))
invoice.add_item(Item(60, 50, description="Item 2", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, 60, description="Item 3", tax=23))
invoice.add_item(Item(50, fullTextSearchInMongo.dbprice, description=fullTextSearchInMongo.dbname, tax=23))

pdf = SimpleInvoice(invoice)
currentDate = datetime.datetime.now().strftime("%H.%M %d-%m-%y")
pdf.gen("faktura " + str(currentDate) + ".pdf", generate_qr_code=True)
