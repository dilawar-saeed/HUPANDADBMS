# Form implementation generated from reading ui file 'c:\Users\ds_sa\Desktop\Fall 23\Database\Project\Order Tracking Form.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 360)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Orders = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.Orders.setGeometry(QtCore.QRect(10, 50, 381, 192))
        self.Orders.setObjectName("Orders")
        self.Orders.setColumnCount(3)
        self.Orders.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Orders.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Orders.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Orders.setHorizontalHeaderItem(2, item)
        self.Feedback = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Feedback.setGeometry(QtCore.QRect(160, 270, 93, 28))
        self.Feedback.setObjectName("Feedback")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.Orders.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "OrderID"))
        item = self.Orders.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total Bill"))
        item = self.Orders.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.Feedback.setText(_translate("MainWindow", "Feedback"))