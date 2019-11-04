from PyQt5 import QtWidgets, QtGui, QtCore
from view import main
import operationsMongo
import customModel


class PythonMongoDB(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(PythonMongoDB, self).__init__()
        self.setupUi(self)

        # data = {'photo': ":/icons/images/photo.jpg",  'name': 'rajiv'}
        # databaseOperations.insert_data(data)

        self.user_data = operationsMongo.getMultipleData()
        self.model = customModel.CustomTableModel(self.user_data)
        self.delegate = customModel.InLineEditDelegate()
        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(self.delegate)
        self.tableView.setItemDelegateForColumn(1, customModel.ProfilePictureDelegate())
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.context_menu)
        self.tableView.verticalHeader().setDefaultSectionSize(50)
        self.tableView.setColumnWidth(0, 30)
        self.tableView.hideColumn(0)
        self.tableView_2.setModel(self.model)
        self.tableView_3.setModel(self.model)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        add_data = menu.addAction("Add New Data")
        add_data.setIcon(QtGui.QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: self.model.insertRows())
        if self.tableView.selectedIndexes():
            remove_data = menu.addAction("Remove Data")
            remove_data.setIcon(QtGui.QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: self.model.removeRows(self.tableView.currentIndex()))
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    my_app = PythonMongoDB()
    my_app.show()
    app.exec_()
