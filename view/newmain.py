# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newmain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 762)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.totalAmountResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalAmountResultLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalAmountResultLabel.setObjectName("totalAmountResultLabel")
        self.gridLayout_3.addWidget(self.totalAmountResultLabel, 5, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/images/app.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.generateInvoiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateInvoiceButton.setObjectName("generateInvoiceButton")
        self.gridLayout_3.addWidget(self.generateInvoiceButton, 6, 0, 1, 1)
        self.totalAmountLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalAmountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalAmountLabel.setObjectName("totalAmountLabel")
        self.gridLayout_3.addWidget(self.totalAmountLabel, 4, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 6, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 3, 1, 1)
        self.clientResultLabel = QtWidgets.QLabel(self.frame)
        self.clientResultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.clientResultLabel.setObjectName("clientResultLabel")
        self.gridLayout_2.addWidget(self.clientResultLabel, 7, 7, 1, 1)
        self.sortClientsByNameButton = QtWidgets.QPushButton(self.frame)
        self.sortClientsByNameButton.setObjectName("sortClientsByNameButton")
        self.gridLayout_2.addWidget(self.sortClientsByNameButton, 2, 4, 1, 1)
        self.tableView_2 = QtWidgets.QTableView(self.frame)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_2.addWidget(self.tableView_2, 0, 4, 1, 4)
        self.searchForClientButton = QtWidgets.QPushButton(self.frame)
        self.searchForClientButton.setObjectName("searchForClientButton")
        self.gridLayout_2.addWidget(self.searchForClientButton, 2, 7, 1, 1)
        self.sortItemsByNameButton = QtWidgets.QPushButton(self.frame)
        self.sortItemsByNameButton.setObjectName("sortItemsByNameButton")
        self.gridLayout_2.addWidget(self.sortItemsByNameButton, 2, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 5, 1, 1)
        self.clientLabel = QtWidgets.QLabel(self.frame)
        self.clientLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.clientLabel.setObjectName("clientLabel")
        self.gridLayout_2.addWidget(self.clientLabel, 6, 7, 1, 1)
        self.tableView = QtWidgets.QTableView(self.frame)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setIconSize(QtCore.QSize(50, 50))
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setObjectName("frame_4")
        self.paymentComboBox = QtWidgets.QComboBox(self.frame_4)
        self.paymentComboBox.setGeometry(QtCore.QRect(0, 30, 61, 20))
        self.paymentComboBox.setObjectName("paymentComboBox")
        self.paymentComboBox.addItem("")
        self.paymentComboBox.addItem("")
        self.paymentLabel = QtWidgets.QLabel(self.frame_4)
        self.paymentLabel.setGeometry(QtCore.QRect(0, 10, 71, 16))
        self.paymentLabel.setObjectName("paymentLabel")
        self.discountLabel = QtWidgets.QLabel(self.frame_4)
        self.discountLabel.setGeometry(QtCore.QRect(0, 52, 71, 16))
        self.discountLabel.setObjectName("discountLabel")
        self.discountSpinBox = QtWidgets.QSpinBox(self.frame_4)
        self.discountSpinBox.setGeometry(QtCore.QRect(0, 70, 61, 22))
        self.discountSpinBox.setObjectName("discountSpinBox")
        self.invoiceGenerationDateLabel = QtWidgets.QLabel(self.frame_4)
        self.invoiceGenerationDateLabel.setGeometry(QtCore.QRect(0, 92, 91, 16))
        self.invoiceGenerationDateLabel.setObjectName("invoiceGenerationDateLabel")
        self.invoiceGenerationDateEdit = QtWidgets.QDateEdit(self.frame_4)
        self.invoiceGenerationDateEdit.setGeometry(QtCore.QRect(0, 110, 61, 22))
        self.invoiceGenerationDateEdit.setObjectName("invoiceGenerationDateEdit")
        self.invoicePaymentDateEdit = QtWidgets.QDateEdit(self.frame_4)
        self.invoicePaymentDateEdit.setGeometry(QtCore.QRect(0, 148, 61, 22))
        self.invoicePaymentDateEdit.setDate(QtCore.QDate(2020, 1, 10))
        self.invoicePaymentDateEdit.setObjectName("invoicePaymentDateEdit")
        self.invoiceGenerationDateLabel_2 = QtWidgets.QLabel(self.frame_4)
        self.invoiceGenerationDateLabel_2.setGeometry(QtCore.QRect(0, 130, 71, 16))
        self.invoiceGenerationDateLabel_2.setObjectName("invoiceGenerationDateLabel_2")
        self.invoiceNumberLabel = QtWidgets.QLabel(self.frame_4)
        self.invoiceNumberLabel.setGeometry(QtCore.QRect(0, 170, 71, 16))
        self.invoiceNumberLabel.setObjectName("invoiceNumberLabel")
        self.invoiceNumberEdit = QtWidgets.QLineEdit(self.frame_4)
        self.invoiceNumberEdit.setGeometry(QtCore.QRect(0, 190, 61, 20))
        self.invoiceNumberEdit.setObjectName("invoiceNumberEdit")
        self.gridLayout_2.addWidget(self.frame_4, 6, 0, 5, 1)
        self.searchForItemButton = QtWidgets.QPushButton(self.frame)
        self.searchForItemButton.setObjectName("searchForItemButton")
        self.gridLayout_2.addWidget(self.searchForItemButton, 2, 0, 1, 1)
        self.tableView_3 = QtWidgets.QTableView(self.frame)
        self.tableView_3.setObjectName("tableView_3")
        self.gridLayout_2.addWidget(self.tableView_3, 10, 2, 1, 6)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Application = QtWidgets.QAction(MainWindow)
        self.actionAbout_Application.setIcon(icon)
        self.actionAbout_Application.setObjectName("actionAbout_Application")
        self.menuAbout.addAction(self.actionAbout_Application)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Invoice App "))
        self.totalAmountResultLabel.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Invoice App"))
        self.generateInvoiceButton.setText(_translate("MainWindow", "Generate Invoice"))
        self.totalAmountLabel.setText(_translate("MainWindow", "Total Amount:"))
        self.pushButton_6.setText(_translate("MainWindow", "Search by NIP"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.clientResultLabel.setText(_translate("MainWindow", "Not selected yet"))
        self.sortClientsByNameButton.setText(_translate("MainWindow", "Sort by name"))
        self.searchForClientButton.setText(_translate("MainWindow", "Search For Client"))
        self.sortItemsByNameButton.setText(_translate("MainWindow", "Sort by Name"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.clientLabel.setText(_translate("MainWindow", "Client:"))
        self.pushButton_4.setText(_translate("MainWindow", "Search by Letter"))
        self.paymentComboBox.setItemText(0, _translate("MainWindow", "Przelew"))
        self.paymentComboBox.setItemText(1, _translate("MainWindow", "Gotówka"))
        self.paymentLabel.setText(_translate("MainWindow", "Płatność:"))
        self.discountLabel.setText(_translate("MainWindow", "Upust:"))
        self.invoiceGenerationDateLabel.setText(_translate("MainWindow", "Data wystawienia:"))
        self.invoiceGenerationDateLabel_2.setText(_translate("MainWindow", "Data płatności:"))
        self.invoiceNumberLabel.setText(_translate("MainWindow", "Nr Faktury:"))
        self.searchForItemButton.setText(_translate("MainWindow", "Search by Name"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAbout_Application.setText(_translate("MainWindow", "About Application"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
