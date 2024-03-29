#próba


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from nmap_window import Ui_NmapWindow
import sys

class Ui_MainWindow(object):
    def openNmapWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NmapWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 600)
        MainWindow.move(100, 100)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_nmap = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openNmapWindow())
        self.pushButton_nmap.setGeometry(QtCore.QRect(140, 110, 221, 51))
        self.pushButton_nmap.setObjectName("pushButton_nmap")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 40, 301, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_johnTheRipper = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_johnTheRipper.setGeometry(QtCore.QRect(140, 190, 221, 51))
        self.pushButton_johnTheRipper.setObjectName("pushButton_johnTheRipper")
        self.pushButton_hashcat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hashcat.setGeometry(QtCore.QRect(140, 270, 221, 51))
        self.pushButton_hashcat.setObjectName("pushButton_hashcat")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(220, 350, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(191, 191, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser_2.setPalette(palette)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(180, 420, 131, 51))
        self.pushButton_quit.setObjectName("pushButton_quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
       ## self.pushButton_quit.pressed.connect(MainWindow.close) # type: ignore
        self.pushButton_quit.pressed.connect(MainWindow.closeEvent)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.closeAllWindows()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_nmap.setText(_translate("MainWindow", "nmap"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Please choose a program:</span></p></body></html>"))
        self.pushButton_johnTheRipper.setText(_translate("MainWindow", "john the ripper"))
        self.pushButton_hashcat.setText(_translate("MainWindow", "hashcat"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">or</span></p></body></html>"))
        self.pushButton_quit.setText(_translate("MainWindow", "quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
  ##  app.aboutToQuit.connect(close_all_window(self))
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
