# Form implementation generated from reading ui file 'c:\Users\ds_sa\Desktop\Fall 23\Database\Project\Recipes.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 423)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IngredientsList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.IngredientsList.setGeometry(QtCore.QRect(10, 100, 421, 271))
        self.IngredientsList.setObjectName("IngredientsList")
        self.bruh = QtWidgets.QLabel(parent=self.centralwidget)
        self.bruh.setGeometry(QtCore.QRect(60, 0, 71, 41))
        self.bruh.setObjectName("bruh")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 171, 41))
        self.label_6.setObjectName("label_6")
        self.ItemName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.ItemName.setGeometry(QtCore.QRect(150, 10, 191, 22))
        self.ItemName.setObjectName("ItemName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 26))
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
        self.bruh.setText(_translate("MainWindow", "Item Name"))
        self.label_6.setText(_translate("MainWindow", "Ingredients Used:"))