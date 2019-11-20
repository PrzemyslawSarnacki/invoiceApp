from PyQt5 import QtWidgets, QtGui, QtCore
from view import tryui
import operationsMongo
import generateInvoice
import customModel
import icons_rc
import datetime


class PythonMongoDB(tryui.Ui_MainWindow, QtWidgets.QMainWindow):
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
        self.tableView_2.customContextMenuRequested.connect(lambda : self.context_menu(self.model_2, self.tableView_2))
        # self.generateInvoiceButton.clicked.connect(lambda : print(j)))
        self.user_data_3 = operationsMongo.Database("TEMPSP").getMultipleData()
        self.model_3 = customModel.CustomTableModel(self.user_data_3, "TEMPSP")
        self.tableView_3.setModel(self.model_3)
        self.tableView_3.setItemDelegate(self.delegate)
        self.tableView_3.hideRow(0)
        self.tableView_3.hideColumn(0)
        self.tableView_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_3.customContextMenuRequested.connect(lambda: self.context_menu(self.model_3, self.tableView_3))
        
        self.user_data_4 = operationsMongo.Database("SP").sortDescending("SP", "NR_KOD")
        self.model_4 = customModel.CustomTableModel(self.user_data_4, "SP")
        self.tableView_4.setModel(self.model_4)
        self.tableView_4.setItemDelegate(self.delegate)
        self.tableView_4.hideColumn(0)
        self.tableView_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_4.customContextMenuRequested.connect(lambda: self.context_menu(self.model_4, self.tableView_4))

        self.generateInvoiceButton.clicked.connect(self.generateInvoiceFinalAction)
        self.searchForItemButton.clicked.connect(lambda : self.searchItemByName(self.model, self.tableView, self.user_data, "ASOR", "NAZWA"))
        self.searchForClientButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "NAZWA_I"))
        self.sortItemsByNameButton.clicked.connect(lambda : self.refreshTable((operationsMongo.Database("ASOR").sortAscending("ASOR", "NAZWA")), 1))
        self.sortClientsByNameButton.clicked.connect(lambda : self.refreshTable((operationsMongo.Database("KONTRAH").sortAscending("KONTRAH", "NAZWA_I")), 2))
        self.searchClientsByNIPButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "REJESTR"))
        self.searchClientByCodeButton.clicked.connect(lambda : self.searchItemByCode(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "NR_KONTRAH"))
        self.searchItemByCodeButton.clicked.connect(lambda : self.searchItemByCode(self.model, self.tableView, self.user_data, "ASOR", "KOD"))
        self.invoiceGenerationDateEdit.setDate(datetime.datetime.now())
        self.invoicePaymentDateEdit.setDate(datetime.datetime.now())
        

    def setClient(self, varModel, varTableView):
        clientName, clientAddress, clientContact = varModel.setClientForInvoice(varTableView.currentIndex())
        PythonMongoDB.invoice = generateInvoice.setClient(clientName, clientAddress, clientContact, '')
        self.clientResultLabel.setText(clientName)
        # you can add here clear
   
    def generateInvoiceFinalAction(self):
        # if not self.invoiceNumberEdit.text():
        #     QtWidgets.QMessageBox.critical(
        #                 self, "Błąd", "Wypełnij komórkę!")
        totalAmount = 0
        taxAmount = 0
        finalInvoiceList = operationsMongo.Database("TEMPSP").getMultipleData()
        discount = self.discountSpinBox.value()
        print(discount)
        listPosition = 0
        for invoiceFinalItem in finalInvoiceList[1:]:
            listPosition += 1
            # itemName = (invoiceFinalItem)["NAZWA"]
            # itemPrice = (invoiceFinalItem)["KOSZT"]
            # itemCode = (invoiceFinalItem)["KOD"]
            vatCondition="PRAWDA"
            tax = invoiceFinalItem["PODAT"]
            if invoiceFinalItem["UPUST"] != 0:
                discount = float(invoiceFinalItem["UPUST"])
            amountOfStuff = float((invoiceFinalItem)["ILOSC"])
            document_id = (invoiceFinalItem)["PREVID"]
            ok = operationsMongo.Database("ASOR").subtractDataFromWarehouse(document_id, PythonMongoDB.invoice, listPosition, amountOfStuff, tax, discount, vatCondition)
            totalAmount += amountOfStuff * (invoiceFinalItem["CENA"])
            taxAmount += 0 if tax == 0 else ((tax/100) * totalAmount)
        try:
            if ok:
                paymentType = self.paymentComboBox.currentText()
                invoiceGenerationDate = self.invoiceGenerationDateEdit.date().toString("dd.MM.yyyy")
                invoicePaymentDate = self.invoicePaymentDateEdit.date().toString("dd.MM.yyyy")
                invoiceSaleDate = self.invoiceSaleDateEdit_2.date().toString("dd.MM.yyyy")
                invoiceNumber = self.invoiceNumberEdit.text()
                invoiceType = self.invoiceTypeComboBox.currentText()
                warehouse = self.warehouseSelectComboBox_3.currentText()
                generateInvoice.createInvoice(PythonMongoDB.invoice, totalAmount, paymentType, invoiceGenerationDate, invoicePaymentDate, invoiceSaleDate, invoiceNumber, discount, tax, invoiceType, taxAmount, warehouse)
                QtWidgets.QMessageBox.information(self, "Ok", "Invoice Created!")
                operationsMongo.Database("TEMPSP").clearTemporaryTableForInvoice()
        except UnboundLocalError:
            QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Wypełnij fakturę!")

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
        elif selectTable == 4:
            self.model_4 = customModel.CustomTableModel(varUserData, "SP")
            self.tableView_4.setModel(self.model_4)

    def searchItemByName(self, varModel, varTableView, varUserData, collectionName, searchedKey):
        searchPhrase, ok = QtWidgets.QInputDialog.getText(self, 'Wprowadz dane', 'Wprowadz dane')
        try:
            if ok:
                self.refreshTable((operationsMongo.Database(collectionName).searchForItem(searchPhrase, collectionName, searchedKey)), selectTable=1)
        except IndexError:
             QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Brak takiej pozycji!")
    
    def searchItemByCode(self, varModel, varTableView, varUserData, collectionName, searchedKey):
        searchPhrase, ok = QtWidgets.QInputDialog.getText(self, 'Wprowadz dane', 'Wprowadz dane')
        try:
            if ok:
                if varModel == self.model:
                    self.refreshTable((operationsMongo.Database(collectionName).searchByNumer(searchPhrase, collectionName, searchedKey)), selectTable=1)
                elif varModel == self.model_2:
                    self.refreshTable((operationsMongo.Database(collectionName).searchByNumer(int(searchPhrase), collectionName, searchedKey)), selectTable=2)
        except IndexError:
             QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Brak takiej pozycji!")
        except ValueError:
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
        if varModel == self.model:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("ASOR").getMultipleData(), 1))
        elif varModel == self.model_2:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("KONTRAH").getMultipleData(), 2))
        elif varModel == self.model_3:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("TEMPSP").getMultipleData(), 3))
        elif varModel == self.model_4:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("SP").sortDescending("SP", "NR_KOD"), 4))
        
        if varModel == self.model:
            add_to_invoice = menu.addAction("Add This To Invoice")
            add_to_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            add_to_invoice.triggered.connect(lambda: self.getAmountOfStuff(varModel, varTableView))
        elif varModel == self.model_2:
            set_client_for_invoice = menu.addAction("Choose this Client")
            set_client_for_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            set_client_for_invoice.triggered.connect(lambda : self.setClient(varModel, varTableView))
        elif varModel == self.model_4:
            show_this_invoice = menu.addAction("Show this invoice")
            show_this_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            show_this_invoice.triggered.connect(lambda : self.refreshTable(varModel.showInvoice(varTableView.currentIndex()), 4))
        if varModel == self.model_4:
            pass
        else:
            add_data = menu.addAction("Add New Data")
            add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            add_data.triggered.connect(lambda: varModel.insertRows())
        
        if varModel == self.model_4:
            pass
        else:
            if varTableView.selectedIndexes():
                remove_data = menu.addAction("Remove Data")
                remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
                remove_data.triggered.connect(lambda: varModel.removeRows(varTableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())
        return PythonMongoDB.invoice
        

if __name__ == '__main__':
    app = QtWidgets.QApplication([]) 
    app.setStyle("Fusion")
    my_app = PythonMongoDB()
    my_app.show()
    app.exec_()
