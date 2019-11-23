from PyQt5 import QtWidgets, QtGui, QtCore
from view import tryui
from view import ItemDialog
import operationsMongo
import generateInvoice
import customModel
import icons_rc
import datetime


class PythonMongoDB(tryui.Ui_MainWindow, QtWidgets.QMainWindow):
    invoice = None
    totalAmount = 0
    nettoAmount = 0

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

        self.tableView_2.setModel(self.model_2)
        self.tableView_2.setItemDelegate(self.delegate)
        self.tableView_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_2.customContextMenuRequested.connect(lambda : self.context_menu(self.model_2, self.tableView_2))
        self.tableView_2.hideColumn(0)
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

        self.model_5 = customModel.CustomTableModel(self.user_data_2, "KONTRAH")
        self.tableView_5.setModel(self.model_5)
        self.tableView_5.setItemDelegate(self.delegate)
        self.tableView_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_5.customContextMenuRequested.connect(lambda: self.context_menu(self.model_5, self.tableView_5))
        
        self.model_6 = customModel.CustomTableModel(self.user_data, "ASOR")
        self.tableView_6.setModel(self.model_6)
        self.tableView_6.setItemDelegate(self.delegate)
        self.tableView_6.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_6.customContextMenuRequested.connect(lambda: self.context_menu(self.model_6, self.tableView_6))
        
        self.user_data_7 = operationsMongo.Database("TEMPKU").getMultipleData()
        self.model_7 = customModel.CustomTableModel(self.user_data_7, "TEMPKU")
        self.tableView_7.setModel(self.model_7)
        self.tableView_7.setItemDelegate(self.delegate)
        self.tableView_7.hideRow(0)
        self.tableView_7.hideColumn(0)
        self.tableView_7.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_7.customContextMenuRequested.connect(lambda: self.context_menu(self.model_7, self.tableView_7))

        self.generateInvoiceButton.clicked.connect(self.generateInvoiceFinalAction)
        self.generateInvoiceButton_2.clicked.connect(self.generatePurchaseInvoiceFinalAction)
        
        self.searchForItemButton.clicked.connect(lambda : self.searchItemByName(self.model, self.tableView, self.user_data, "ASOR", "NAZWA"))
        self.searchItemByCodeButton.clicked.connect(lambda : self.searchItemByCode(self.model, self.tableView, self.user_data, "ASOR", "KOD"))
        self.searchItemByGroupButton.clicked.connect(lambda : self.searchItemByName(self.model, self.tableView, self.user_data, "ASOR", "GRUPA"))
        # self.searchItemsByCityButton.clicked.connect(self.openAddItemWindow)
        
        self.searchForClientButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "NAZWA_I"))
        self.searchClientsByNIPButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "REJESTR"))
        self.searchClientByCodeButton.clicked.connect(lambda : self.searchItemByCode(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "NR_KONTRAH"))
        self.searchClientsByCityButton.clicked.connect(lambda : self.searchClientByName(self.model_2, self.tableView_2, self.user_data_2, "KONTRAH", "MIEJSC"))
        
        self.searchForItemButton_2.clicked.connect(lambda : self.searchItemByName(self.model_6, self.tableView_6, self.user_data, "ASOR", "NAZWA"))
        self.searchItemByCodeButton_2.clicked.connect(lambda : self.searchItemByCode(self.model_6, self.tableView_6, self.user_data, "ASOR", "KOD"))
        self.searchItemByGroupButton_2.clicked.connect(lambda : self.searchItemByName(self.model_6, self.tableView_6, self.user_data, "ASOR", "GRUPA"))
        # self.searchItemsByCityButton.clicked.connect(self.openAddItemWindow)
        
        self.searchForClientButton_2.clicked.connect(lambda : self.searchClientByName(self.model_5, self.tableView_5, self.user_data_2, "KONTRAH", "NAZWA_I"))
        self.searchClientsByNIPButton_2.clicked.connect(lambda : self.searchClientByName(self.model_5, self.tableView_5, self.user_data_2, "KONTRAH", "REJESTR"))
        self.searchClientByCodeButton_2.clicked.connect(lambda : self.searchItemByCode(self.model_5, self.tableView_5, self.user_data_2, "KONTRAH", "NR_KONTRAH"))
        self.searchClientsByCityButton_2.clicked.connect(lambda : self.searchClientByName(self.model_5, self.tableView_5, self.user_data_2, "KONTRAH", "MIEJSC"))
        
        self.invoiceGenerationDateEdit.setDate(datetime.datetime.now())
        self.invoicePaymentDateEdit.setDate(datetime.datetime.now())
        self.invoiceSaleDateEdit_2.setDate(datetime.datetime.now())
        self.invoiceGenerationDateEdit_2.setDate(datetime.datetime.now())
        self.invoicePaymentDateEdit_2.setDate(datetime.datetime.now())
        self.invoiceSaleDateEdit_3.setDate(datetime.datetime.now())
        self.documentsTypeComboBox.currentTextChanged.connect(lambda: self.refreshTable(operationsMongo.Database(self.setDocumentPreview()).sortDescending(self.setDocumentPreview(), "NR_KOD"), 4))
        self.invoiceTypeComboBox.currentTextChanged.connect(self.setInvoiceNumberLine)

    def openAddItemWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = ItemDialog.Ui_ItemDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def setDocumentPreview(self):
        if self.documentsTypeComboBox.currentText() == "Purchase Invoices":
            halfOfCollectionName = "KU"
        elif self.documentsTypeComboBox.currentText() == "Invoices":
            halfOfCollectionName = "SP"
        elif self.documentsTypeComboBox.currentText() == "PZ":
            halfOfCollectionName = "PZ"
        elif self.documentsTypeComboBox.currentText() == "WZ":
            halfOfCollectionName = "WZ"
        elif self.documentsTypeComboBox.currentText() == "RW":
            halfOfCollectionName = "RW"
        elif self.documentsTypeComboBox.currentText() == "MM":
            halfOfCollectionName = "MM"
        elif self.documentsTypeComboBox.currentText() == "Settlement":
            halfOfCollectionName = "ROZLICZE"
        elif self.documentsTypeComboBox.currentText() == "Warehouse Cards":
            halfOfCollectionName = "KARTA2"
        return halfOfCollectionName
    
    def setInvoiceNumberLine(self):
        if self.invoiceTypeComboBox.currentText() == "Hurtowa":
            numberString = "H" + str(operationsMongo.Database("SP").getSingleLastData()["NUMER"] + 1) + "/1"
            self.invoiceNumberEdit.setText(numberString)
        elif self.invoiceTypeComboBox.currentText() == "PW":
            numberString = "H" + str(operationsMongo.Database("SP").getSingleLastData()["NUMER"] + 1) + "/1"
            self.invoiceNumberEdit.setText(numberString)
        
    def setClient(self, varModel, varTableView):
        clientName, clientAddress, clientContact = varModel.setClientForInvoice(varTableView.currentIndex())
        if varModel == self.model_5:
            self.clientResultLabel_2.setText(clientName)
        elif varModel == self.model_2:
            self.clientResultLabel.setText(clientName)
            PythonMongoDB.invoice = generateInvoice.setClient(clientName, clientAddress, clientContact, '')
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
                priceType = self.priceTypeComboBox.currentText()
                generateInvoice.createInvoice(PythonMongoDB.invoice, totalAmount, paymentType, invoiceGenerationDate, invoicePaymentDate, invoiceSaleDate, invoiceNumber, discount, tax, invoiceType, taxAmount, warehouse, priceType)
                QtWidgets.QMessageBox.information(self, "Ok", "Invoice Created!")
                operationsMongo.Database("TEMPSP").clearTemporaryTableForInvoice()
        except UnboundLocalError:
            QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Wypełnij fakturę!")
   
    def generatePurchaseInvoiceFinalAction(self):
        # if not self.invoiceNumberEdit.text():
        #     QtWidgets.QMessageBox.critical(
        #                 self, "Błąd", "Wypełnij komórkę!")
        totalAmount = 0
        taxAmount = 0
        finalInvoiceList = operationsMongo.Database("TEMPKU").getMultipleData()
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
            ok = operationsMongo.Database("ASOR").addDataToWarehouse(document_id, listPosition, amountOfStuff)
            totalAmount += amountOfStuff * (invoiceFinalItem["CENA"])
            taxAmount += 0 if tax == 0 else ((tax/100) * totalAmount)
        try:
            if ok:
                paymentType = self.paymentComboBox_2.currentText()
                invoiceGenerationDate = self.invoiceGenerationDateEdit_2.date().toString("dd.MM.yyyy")
                invoicePaymentDate = self.invoicePaymentDateEdit_2.date().toString("dd.MM.yyyy")
                invoiceInflowDate = self.invoiceSaleDateEdit_3.date().toString("dd.MM.yyyy")
                invoiceNumber = self.invoiceNumberEdit_2.text()
                invoiceType = self.invoiceTypeComboBox_4.currentText()
                warehouse = self.warehouseSelectComboBox_3.currentText()
                priceType = self.priceTypeComboBox_2.currentText()
                clientName = self.clientResultLabel_2.text()
                operationsMongo.Database("KU").createPurchaseInvoice(totalAmount, clientName, invoiceGenerationDate, invoiceInflowDate, discount, invoicePaymentDate, invoiceNumber, invoiceType, warehouse, priceType, paymentType)
                QtWidgets.QMessageBox.information(self, "Ok", "Invoice Created!")
                operationsMongo.Database("TEMPKU").clearTemporaryTableForPurchaseInvoice()
        except UnboundLocalError:
            QtWidgets.QMessageBox.critical(
                        self, "Błąd", "Wypełnij fakturę!")

    def getAmountOfStuff(self, varModel, varTableView):
        if PythonMongoDB.invoice != None or self.clientResultLabel_2 != "Not selected yet":
            amountOfStuff, ok = QtWidgets.QInputDialog.getDouble(self, 'Wprowadz dane', 'Wprowadz dane')
            if ok:
                QtWidgets.QMessageBox.information(self, "Ok", "Ok!")
                if varModel == self.model:
                    tempList = "TEMPSP"
                elif varModel == self.model_6:
                    tempList = "TEMPKU"
                itemAndCountMultiplied = varModel.addRowsToInvoice(varTableView.currentIndex(), amountOfStuff, tempList)
                PythonMongoDB.nettoAmount += itemAndCountMultiplied 
                PythonMongoDB.totalAmount += (itemAndCountMultiplied + (itemAndCountMultiplied * 0.23))
                if tempList == "TEMPSP":
                    self.refreshTable(operationsMongo.Database(tempList).getMultipleData(), selectTable=3)   
                    self.nettoAmountResultLabel.setText(str(PythonMongoDB.nettoAmount))
                    self.totalAmountResultLabel.setText(str(PythonMongoDB.totalAmount))
                elif tempList == "TEMPKU":
                    self.refreshTable(operationsMongo.Database(tempList).getMultipleData(), selectTable=7)   
                    self.nettoAmountResultLabel_2.setText(str(PythonMongoDB.nettoAmount))
                    self.totalAmountResultLabel_2.setText(str(PythonMongoDB.totalAmount))
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
            self.model_4 = customModel.CustomTableModel(varUserData, self.setDocumentPreview())
            self.tableView_4.setModel(self.model_4)
        elif selectTable == 5:
            self.model_5 = customModel.CustomTableModel(varUserData, "KONTRAH")
            self.tableView_5.setModel(self.model_5)
        elif selectTable == 6:
            self.model_6 = customModel.CustomTableModel(varUserData, "ASOR")
            self.tableView_6.setModel(self.model_6)
        elif selectTable == 7:
            self.model_7 = customModel.CustomTableModel(varUserData, "TEMPKU")
            self.tableView_7.setModel(self.model_7)

    def searchItemByName(self, varModel, varTableView, varUserData, collectionName, searchedKey):
        searchPhrase, ok = QtWidgets.QInputDialog.getText(self, 'Wprowadz dane', 'Wprowadz dane')
        try:
            if ok:
                if varModel == self.model:
                    self.refreshTable((operationsMongo.Database(collectionName).searchForItem(searchPhrase, collectionName, searchedKey)), selectTable=1)
                elif varModel == self.model_6:
                    self.refreshTable((operationsMongo.Database(collectionName).searchForItem(searchPhrase, collectionName, searchedKey)), selectTable=6)
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
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database(self.setDocumentPreview()).sortDescending(self.setDocumentPreview(), "NR_KOD"), 4))
        elif varModel == self.model_5:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("KONTRAH").getMultipleData(), 5))
        elif varModel == self.model_6:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("ASOR").getMultipleData(), 6))
        elif varModel == self.model_7:
            refresh_data.triggered.connect(lambda: self.refreshTable(operationsMongo.Database("TEMPKU").getMultipleData(), 7))
        
        if varModel == self.model:
            add_to_invoice = menu.addAction("Add This To Invoice")
            add_to_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            add_to_invoice.triggered.connect(lambda: self.getAmountOfStuff(varModel, varTableView))
        elif varModel == self.model_2:
            set_client_for_invoice = menu.addAction("Choose this Client")
            set_client_for_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            set_client_for_invoice.triggered.connect(lambda : self.setClient(varModel, varTableView))
        elif varModel == self.model_6:
            add_to_invoice = menu.addAction("Add This To Invoice")
            add_to_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            add_to_invoice.triggered.connect(lambda: self.getAmountOfStuff(varModel, varTableView))
        elif varModel == self.model_5:
            set_client_for_invoice = menu.addAction("Choose this Client")
            set_client_for_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            set_client_for_invoice.triggered.connect(lambda : self.setClient(varModel, varTableView))
        elif varModel == self.model_4:
            show_this_invoice = menu.addAction("Show this invoice")
            show_this_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
            show_this_invoice.triggered.connect(lambda : self.refreshTable(varModel.showInvoice(varTableView.currentIndex(), self.setDocumentPreview()), 4))
        
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
