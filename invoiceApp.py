from PyQt5 import QtWidgets, QtGui, QtCore
from view import main
import operationsMongo
import generateInvoice
import customModel
import icons_rc


class PythonMongoDB(main.Ui_MainWindow, QtWidgets.QMainWindow):
    invoice = None

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
        self.tableView.customContextMenuRequested.connect(lambda: self.context_menu(self.model, self.tableView, self.user_data))
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
        self.tableView_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView_3.customContextMenuRequested.connect(lambda: self.context_menu(self.model_3, self.tableView_3, self.user_data_3))
        self.generateInvoiceButton.clicked.connect(lambda : generateInvoice.createInvoice(PythonMongoDB.invoice))

    def context_menu_client(self, varModel , varTableView):
        menu = QtWidgets.QMenu()
        set_client_for_invoice = menu.addAction("Choose this Client")
        set_client_for_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        x = lambda : (varModel.setClientForInvoice(varTableView.currentIndex()))
        set_client_for_invoice.triggered.connect(x)
        clientName, clientAddress, clientContact = x()
        PythonMongoDB.invoice = generateInvoice.setClient(clientName, clientAddress, clientContact, '')
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

    def context_menu(self, varModel, varTableView, varUserData):
        menu = QtWidgets.QMenu()
        refresh_data = menu.addAction("Refresh Data")
        if refresh_data.triggered.connect(lambda: self):
            self.user_data_3 = operationsMongo.Database("TEMPSP").getMultipleData()
            self.model_3 = customModel.CustomTableModel(self.user_data_3, "TEMPSP")
            self.tableView_3.setModel(self.model_3)
        add_to_invoice = menu.addAction("Add This To Invoice")
        add_to_invoice.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_to_invoice.triggered.connect(lambda: varModel.addRowsToInvoice(varTableView.currentIndex(), PythonMongoDB.invoice))
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
