import generateInvoice

invoice = generateInvoice.setClient('Adfasd', 'efFdsf', 'AFAAF', '')

while True:
    inp = input()
    if inp == '1':
        generateInvoice.createInvoice(invoice)
        break
    else:
        generateInvoice.addItemToInvoice(invoice, 40, 'oł je', 500)
