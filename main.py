from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QAction, QTabBar, QPushButton
from PyQt5 import uic
import sys
from file_chooser import Ui_MainWindow

class main_window(QMainWindow):

    def open_file_chooser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self):
        super(main_window, self).__init__()
        uic.loadUi("main_window.ui", self)
        self.show()

class file_chooser(QMainWindow):
    def __init__(self):
        super(file_chooser, self).__init__()
        uic.loadUi("file_chooser.ui", self)
        self.show()

class file_viewer(QMainWindow):
    def __init__(self):
        super(file_viewer, self).__init__()
        uic.loadUi("file_chooser.ui", self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UiWindow = main_window()
    #UiWindow = file_chooser()
    UiWindow.show()
    sys.exit(app.exec())






