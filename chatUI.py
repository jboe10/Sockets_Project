# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jboes\Desktop\chatClient.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(303, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Send message button
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(51, 300, 200, 31))
        self.sendBtn.setObjectName("sendBtn")

        # Chat log (list)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(23, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")

        # Chat Input
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(23, 220, 256, 71))
        self.lineEdit.setObjectName("lineEdit")

        # Connect Client to Server Button
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(51, 340, 75, 23))
        self.connectButton.setObjectName("connectButton")

        # Disconnect from server
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(176, 340, 75, 23))
        self.disconnectButton.setObjectName("disconnectButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        ##################### Button Click Actions ############################
        self.sendBtn.clicked.connect(self.addItem)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendBtn.setText(_translate("MainWindow", "Send"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))

    def addItem(self):
        value = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

