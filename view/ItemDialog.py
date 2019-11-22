# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ItemDialog(object):
    def setupUi(self, ItemDialog):
        ItemDialog.setObjectName("ItemDialog")
        ItemDialog.resize(430, 290)
        self.buttonBox = QtWidgets.QDialogButtonBox(ItemDialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 250, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.nameLabel = QtWidgets.QLabel(ItemDialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 25, 71, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(ItemDialog)
        self.nameLineEdit.setGeometry(QtCore.QRect(110, 25, 113, 20))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.priceLabel_2 = QtWidgets.QLabel(ItemDialog)
        self.priceLabel_2.setGeometry(QtCore.QRect(240, 25, 71, 20))
        self.priceLabel_2.setObjectName("priceLabel_2")
        self.currencyLabel_3 = QtWidgets.QLabel(ItemDialog)
        self.currencyLabel_3.setGeometry(QtCore.QRect(330, 25, 71, 20))
        self.currencyLabel_3.setObjectName("currencyLabel_3")
        self.currencyLineEdit_3 = QtWidgets.QLineEdit(ItemDialog)
        self.currencyLineEdit_3.setGeometry(QtCore.QRect(330, 49, 81, 20))
        self.currencyLineEdit_3.setObjectName("currencyLineEdit_3")
        self.priceDoubleSpinBox = QtWidgets.QDoubleSpinBox(ItemDialog)
        self.priceDoubleSpinBox.setGeometry(QtCore.QRect(240, 50, 81, 22))
        self.priceDoubleSpinBox.setObjectName("priceDoubleSpinBox")

        self.retranslateUi(ItemDialog)
        self.buttonBox.accepted.connect(ItemDialog.accept)
        self.buttonBox.rejected.connect(ItemDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ItemDialog)

    def retranslateUi(self, ItemDialog):
        _translate = QtCore.QCoreApplication.translate
        ItemDialog.setWindowTitle(_translate("ItemDialog", "Dialog"))
        self.nameLabel.setText(_translate("ItemDialog", "Nazwa towaru"))
        self.priceLabel_2.setText(_translate("ItemDialog", "Koszt"))
        self.currencyLabel_3.setText(_translate("ItemDialog", "Waluta:"))
        self.currencyLineEdit_3.setText(_translate("ItemDialog", "PZL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ItemDialog = QtWidgets.QDialog()
    ui = Ui_ItemDialog()
    ui.setupUi(ItemDialog)
    ItemDialog.show()
    sys.exit(app.exec_())
