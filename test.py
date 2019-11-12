# import generateInvoice

class UnicodeProperty(object):
    _attrs = ()

    def __setattr__(self, key, value):
        if key in self._attrs:
            value = value
        self.__dict__[key] = value


class Client(client):
    pass

class Invoice(UnicodeProperty):
    """
    Invoice definition

    :param client: client of the invoice
    :type client: Client
    :param creator: creator of the invoice
    :type creator: Kreator
    :param provider: provider of the invoice
    :type provider: Provider
    """

    def __init__(self, client):
        assert isinstance(client, Client)

        self.client = client



clientName = "Ja jestem piekny"
client = Client(clientName)
invoice = Invoice(client)
print(invoice)