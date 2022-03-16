
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QFileDialog, QDialog
import sys
#from PyQt5.uic import loadUi

class file_chooser_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 192)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(50, 119, 261, 31))
        self.file_name.setObjectName("file_name")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(340, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_browse.setFont(font)
        self.pushButton_browse.setObjectName("pushButton_browse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_browse.clicked.connect(self.clicker)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicker(self):
        fname = QFileDialog.getOpenFileName()
        if fname:
            print(str(fname))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = file_chooser_Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
