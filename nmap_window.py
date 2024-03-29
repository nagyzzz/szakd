
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NmapWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 600)
        MainWindow.move(700, 100)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_nmap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nmap.setGeometry(QtCore.QRect(140, 40, 221, 51))
        self.pushButton_nmap.setObjectName("pushButton_nmap")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(170, 470, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.textEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_password.setGeometry(QtCore.QRect(60, 120, 411, 41))
        self.textEdit_password.setToolTip("")
        self.textEdit_password.setStatusTip("")
        self.textEdit_password.setObjectName("textEdit_password")
        self.textEdit_options = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_options.setGeometry(QtCore.QRect(60, 190, 411, 41))
        self.textEdit_options.setToolTip("")
        self.textEdit_options.setStatusTip("")
        self.textEdit_options.setObjectName("textEdit_options")
        self.checkBox_sC = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sC.setGeometry(QtCore.QRect(210, 340, 61, 41))
        self.checkBox_sC.setObjectName("checkBox_sC")
        self.checkBox_sS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sS.setGeometry(QtCore.QRect(210, 390, 61, 41))
        self.checkBox_sS.setObjectName("checkBox_sS")
        self.textEdit_target_ip = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_target_ip.setGeometry(QtCore.QRect(60, 260, 411, 41))
        self.textEdit_target_ip.setToolTip("")
        self.textEdit_target_ip.setStatusTip("")
        self.textEdit_target_ip.setObjectName("textEdit_target_ip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_quit.pressed.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_nmap.setText(_translate("MainWindow", "Run Nmap"))
        self.pushButton_quit.setText(_translate("MainWindow", "quit"))
        self.checkBox_sC.setText(_translate("MainWindow", "-sC"))
        self.checkBox_sS.setText(_translate("MainWindow", "-sS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_NmapWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
