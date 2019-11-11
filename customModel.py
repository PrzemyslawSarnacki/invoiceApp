from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import operationsMongo
import generateInvoice

class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, collectionName):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.collection = collectionName
        self.columns = list(self.user_data[0].keys())

    def flags(self, index):
        """
        Make table editable.
        make first column non editable
        :param index:
        :return:
        """
        if index.column() > 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        elif index.column() == 1:
            return QtCore.Qt.DecorationRole
        else:
            return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        """
        set row counts
        :param args:
        :param kwargs:
        :return:
        """
        return len(self.user_data)

    def columnCount(self, *args, **kwargs):
        """
        set column counts
        :param args:
        :param kwargs:
        :return:
        """
        return len(self.columns)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """
        set column header data
        :param section:
        :param orientation:
        :param role:
        :return:
        """
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[section].title()

    def data(self, index, role):
        """
        Display Data in table cells
        :param index:
        :param role:
        :return:
        """
        row = self.user_data[index.row()]
        column = self.columns[index.column()]
        try:
            if index.column() == 1:
                selected_row = self.user_data[index.row()]
            #     image_data = selected_row['photo']
            #     image = QtGui.QImage()
            #     image.loadFromData(image_data)
            #     icon = QtGui.QIcon()
            #     icon.addPixmap(QtGui.QPixmap.fromImage(image))
            #     return icon
            if role == QtCore.Qt.DisplayRole:
                return str(row[column])
        except KeyError:
            return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        """
        Edit data in table cells
        :param index:
        :param value:
        :param role:
        :return:
        """
        if index.isValid():
            selected_row = self.user_data[index.row()]
            selected_column = self.columns[index.column()]
            selected_row[selected_column] = value
            self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
            ok = operationsMongo.Database(self.collection).updateData(selected_row['_id'], selected_row)
            if ok:
                return True
        return False

    def insertRows(self):
        row_count = len(self.user_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
        empty_data = { key: None for key in self.columns if not key=='_id'}
        document_id = operationsMongo.Database(self.collection).insertData(empty_data)
        new_data = operationsMongo.Database(self.collection).getSingleData(document_id)
        self.user_data.append(new_data)
        row_count += 1
        self.endInsertRows()
        return True

    def removeRows(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.user_data[row_id]['_id']
        operationsMongo.Database(self.collection).removeData(document_id)
        self.user_data.pop(row_id)
        self.endRemoveRows()
        return True
    
    
    def setClientForInvoice(self, position):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.user_data[row_id]['_id']
        clientName = (operationsMongo.Database(self.collection).getSingleData(document_id)["NAZWA_I"])
        clientAddress = str(operationsMongo.Database(self.collection).getSingleData(document_id)["MIEJSC"]) + ' ' +str(operationsMongo.Database(self.collection).getSingleData(document_id)["ADRES"])
        clientContact = (operationsMongo.Database(self.collection).getSingleData(document_id)["TELEFONY"])
        print(clientName, clientAddress, clientContact) 
        return clientName, clientAddress, clientContact
    
    
    def addRowsToInvoice(self, position, invoice, amountOfStuff):
        row_count = self.rowCount()
        row_count -= 1
        self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
        row_id = position.row()
        document_id = self.user_data[row_id]['_id']
        operationsMongo.Database(self.collection).subtractDataFromWarehouse(document_id, invoice, amountOfStuff)
        # operationsMongo.Database(self.collection).addDataToInvoiceList(document_id, invoice,1)
        itemName = (operationsMongo.Database(self.collection).getSingleData(document_id)["NAZWA"])
        itemPrice = (operationsMongo.Database(self.collection).getSingleData(document_id)["KOSZT"])
        itemCode = (operationsMongo.Database(self.collection).getSingleData(document_id)["KOD"])
        # invoiceCode = Database("SPZAW").getSingleLastData()  
        operationsMongo.Database("TEMPSP").insertData({"NR_KOD":649,"LP":1,"LEK": itemName,"NUMER":'null',"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":float(amountOfStuff)*float(itemPrice),"KOD": itemCode,"JEST_VAT":"PRAWDA","PODAT":23.0,"UPUST":0.0})
        operationsMongo.Database("SPZAW").insertData({"NR_KOD":649,"LP":1,"LEK": itemName,"NUMER":'null',"CENA":itemPrice,"ILOSC":amountOfStuff,"WARTOSC":float(amountOfStuff)*float(itemPrice),"KOD":itemCode,"JEST_VAT":"PRAWDA","PODAT":23.0,"UPUST":0.0})
        # operationsMongo.Database("TEMPSP").getMultipleData()

        return True


class ProfilePictureDelegate(QtWidgets.QStyledItemDelegate):
    """
    This will open QFileDialog to select image
    """
    def __init__(self):
        QtWidgets.QStyledItemDelegate.__init__(self)

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QFileDialog()
        return editor

    def setModelData(self, editor, model, index):
        selected_file =editor.selectedFiles()[0]
        image = open(selected_file, 'rb').read()
        model.setData(index, image)


class InLineEditDelegate(QtWidgets.QItemDelegate):
    """
    Delegate is important for inline editing of cells
    """

    def createEditor(self, parent, option, index):
        return super(InLineEditDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        text = index.data(QtCore.Qt.EditRole) or index.data(QtCore.Qt.DisplayRole)
        editor.setText(str(text))
