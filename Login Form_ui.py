# Form implementation generated from reading ui file 'c:\Users\ds_sa\Desktop\Fall 23\Database\Project\Login Form.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 451)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 280, 61, 16))
        self.label_2.setObjectName("label_2")
        self.Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(110, 270, 281, 22))
        self.Password.setObjectName("Password")
        self.userID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.userID.setGeometry(QtCore.QRect(110, 220, 281, 22))
        self.userID.setObjectName("userID")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(35, 20, 361, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 161, 16))
        self.label_3.setObjectName("label_3")
        self.LoginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(290, 330, 93, 28))
        self.LoginButton.setObjectName("LoginButton")
        self.SignUpButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(170, 330, 93, 28))
        self.SignUpButton.setObjectName("SignUpButton")
        self.AdminButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AdminButton.setGeometry(QtCore.QRect(50, 330, 93, 28))
        self.AdminButton.setObjectName("AdminButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 26))
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
        self.label.setText(_translate("MainWindow", "ID: "))
        self.label_2.setText(_translate("MainWindow", "Password: "))
        self.label_3.setText(_translate("MainWindow", "HABIB UNIVERSITY LOGO"))
        self.LoginButton.setText(_translate("MainWindow", "Log In"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.AdminButton.setText(_translate("MainWindow", "Admin"))
