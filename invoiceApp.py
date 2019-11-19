from PyQt5 import QtWidgets, QtGui, QtCore
from view import newmain
import operationsMongo
import generateInvoice
import customModel
import icons_rc


class PythonMongoDB(newmain.Ui_MainWindow, QtWidgets.QMainWindow):
    invoice = None
    totalAmount = 0

    def __init__(self):
        super(PythonMongoDB, self).__init__()
        self.setupUi(self)
        # self.invoice = invoice
        self.user_data = operationsMongo.Database("ASOR").getMultipleData()
        self.user_data_2 = operationsMongo.Database("KONTRAH").getMultipleData()
        self.model = customModel.CustomTableModel(self.user_data, "ASOR")
        self.model_2 = customModel.CustomTableModel(self.user_data_2, "KONTRAH")
        self.delegate = customModel.InLineEditDelegate()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(self.delegate)
        # self.tableView.setItemDelegateForColumn(1, customModel.ProfilePictureDelegate())
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(lambda: self.context_menu(self.model, self.tableView))
        self.tableView.verticalHeader().setDefaultSectionSize(50)
        self.tableView.setColumnWidth(0, 30)
        self.tableView.hideColumn(0)
        self.tableView.hideColumn(2)
        self.tableView.hideColumn(3)
        self.tableView.hideColumn(4)
        self.tableView.hideColumn(14)
        self.tableView.hideColumn(15)
        self.tableView.hideColumn(16)
        # self.tableView.hideColumn(7)
        self.tableView_2.setModel(self.model_2)
        self.tableView_2.setItemDelegate(self.delegate)
        self.tableView_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_2.customContextMenuRequested.connect(lambda : self.context_menu_client(self.model_2, self.tableView_2))
        # self.generateInvoiceButton.clicked.connect(lambda : print(j)))
        self.user_data_3 = operationsMongo.Database("TEMPSP").getMultipleData()
        self.model_3 = customModel.CustomTableModel(self.user_data_3, "TEMPSP")
        self.tableView_3.setModel(self.model_3)
        self.tableView_3.setItemDelegate(self.delegate)
        self.tableView_3.hideRow(0)
        self.tableView_3.hideColumn(0)
        self.tableView_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_3.customContextMenuRequested.connect(lambda: self.context_menu(self.model_3, self.tableView_3))
        self.generateInvoiceButton.clicked.connect(self.generateInvoiceFinalAction)
        self.searchForItemButton.clicked.connect(lambda : self.searchItemByName(self.model, self.tableView, self.user_data, "ASOR", "NAZWA"))
        self.searchForClientButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "NAZWA_I"))
        self.sortItemsByNameButton.clicked.connect(lambda : self.refreshTable((operationsMongo.Database("ASOR").sortAlphabetically("ASOR", "NAZWA")), 1))
        self.sortClientsByNameButton.clicked.connect(lambda : self.refreshTable((operationsMongo.Database("KONTRAH").sortAlphabetically("KONTRAH", "NAZWA_I")), 2))
        self.searchClientsByNIPButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "REJESTR"))

    def context_menu_client(self, varModel , varTableView):
        menu = QtWidgets.QMenu()
        set_client_for_invoice = menu.addAction("Choose this Client")
        set_client_for_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        set_client_for_invoice.triggered.connect(lambda : self.setClient(varModel, varTableView))
        # debug = menu.addAction("Debug")
        # debug.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        # debug.triggered.connect(lambda: print(y))
        add_data = menu.addAction("Add New Data")
        add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: varModel.insertRows())
        if varTableView.selectedIndexes():
            remove_data = menu.addAction("Remove Data")
            remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: varModel.removeRows(varTableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
        return PythonMongoDB.invoice

    def setClient(self, varModel, varTableView):
        clientName, clientAddress, clientContact = varModel.setClientForInvoice(varTableView.currentIndex())
        PythonMongoDB.invoice = generateInvoice.setClient(clientName, clientAddress, clientContact, '')
        self.clientResultLabel.setText(clientName)
        # you can add here clear

    def generateInvoiceFinalAction(self):
        totalAmount = 0
        finalInvoiceList = operationsMongo.Database("TEMPSP").getMultipleData()
        for invoiceFinalItem in finalInvoiceList[1:]:
            # itemName = (invoiceFinalItem)["NAZWA"]
            # itemPrice = (invoiceFinalItem)["KOSZT"]
            # itemCode = (invoiceFinalItem)["KOD"]
            amountOfStuff = float((invoiceFinalItem)["ILOSC"])
            document_id = (invoiceFinalItem)["PREVID"]
            ok, itemAndCountMultiplied = operationsMongo.Database("ASOR").subtractDataFromWarehouse(document_id, PythonMongoDB.invoice, amountOfStuff)
            totalAmount += itemAndCountMultiplied
        if ok:
            generateInvoice.createInvoice(PythonMongoDB.invoice, totalAmount)
            QtWidgets.QMessageBox.information(self, "Ok", "Invoice Created!")
            operationsMongo.Database("TEMPSP").clearTemporaryTableForInvoice()

    def getAmountOfStuff(self, varModel, varTableView):
        if PythonMongoDB.invoice != None:
            amountOfStuff, ok = QtWidgets.QInputDialog.getDouble(self, 'Wprowadz dane', 'Wprowadz dane')
            if ok:
                QtWidgets.QMessageBox.information(self, "Ok", "Ok!")
                itemAndCountMultiplied = varModel.addRowsToInvoice(varTableView.currentIndex(), PythonMongoDB.invoice, amountOfStuff)
                PythonMongoDB.totalAmount += itemAndCountMultiplied
                self.totalAmountResultLabel.setText(str(PythonMongoDB.totalAmount))
                self.refreshTable(operationsMongo.Database("TEMPSP").getMultipleData(), selectTable=3)   
        else:
            QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Wybierz Klienta!")
        
    def refreshTable(self, operation, selectTable):
        varUserData = operation
        if selectTable == 1:
            self.model = customModel.CustomTableModel(varUserData, "ASOR")
            self.tableView.setModel(self.model)
        elif selectTable == 2:
            self.model_2 = customModel.CustomTableModel(varUserData, "KONTRAH")
            self.tableView_2.setModel(self.model_2)
        elif selectTable == 3:
            self.model_3 = customModel.CustomTableModel(varUserData, "TEMPSP")
            self.tableView_3.setModel(self.model_3)
        

    def searchItemByName(self, varModel, varTableView, varUserData, collectionName, searchedKey):
        searchPhrase, ok = QtWidgets.QInputDialog.getText(self, 'Wprowadz dane', 'Wprowadz dane')
        try:
            if ok:
                self.refreshTable((operationsMongo.Database(collectionName).searchForItem(searchPhrase, collectionName, searchedKey)), selectTable=1)
        except IndexError:
             QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Brak takiej pozycji!")
    
    def searchClientByName(self, varModel, varTableView, varUserData, collectionName, searchedKey):
        searchPhrase, ok = QtWidgets.QInputDialog.getText(self, 'Wprowadz dane', 'Wprowadz dane')
        try:
            if ok:
                self.refreshTable((operationsMongo.Database(collectionName).searchForItem(searchPhrase, collectionName, searchedKey)), selectTable=2)
        except IndexError:
             QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Brak takiej pozycji!")
    
    def context_menu(self, varModel, varTableView):
        menu = QtWidgets.QMenu()
        refresh_data = menu.addAction("Refresh Data")
        if refresh_data.triggered.connect(lambda: self):
            self.user_data_3 = operationsMongo.Database("TEMPSP").getMultipleData()
            self.model_3 = customModel.CustomTableModel(self.user_data_3, "TEMPSP")
            self.tableView_3.setModel(self.model_3)
        add_to_invoice = menu.addAction("Add This To Invoice")
        add_to_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_to_invoice.triggered.connect(lambda: self.getAmountOfStuff(varModel, varTableView))
        add_data = menu.addAction("Add New Data")
        add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: varModel.insertRows())
        if varTableView.selectedIndexes():
            remove_data = menu.addAction("Remove Data")
            remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: varModel.removeRows(varTableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
    
    
        

if __name__ == '__main__':
    app = QtWidgets.QApplication([]) 
    app.setStyle("Fusion")
    my_app = PythonMongoDB()
    my_app.show()
    app.exec_()
