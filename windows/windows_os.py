import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from app.gui import Ui_MainWindow


class Windows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

    def load_gui_change(self):
        self.ui.title.setStyleSheet("background-color: red;")







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    alpha = Windows()
    alpha.show()
    sys.exit(app.exec_())
    