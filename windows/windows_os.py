import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from app.gui import Ui_MainWindow


class Windows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()

    def load_gui_change(self):
        self.ui.download_mp3.setStyleSheet("background-color: #0b78a3;")
        self.ui.download_mp3.setGeometry(QtCore.QRect(640, 230, 140, 40))            
        self.ui.download_video_btn.setStyleSheet("background-color: #0b78a3;")   
        self.ui.download_video_btn.setGeometry(QtCore.QRect(20, 230, 140, 40))                 
        self.ui.title.setStyleSheet("background-color: #0b78a3; color: white;")
        self.ui.sub_title.setStyleSheet("color: #2a5c49")
        self.ui.retype.setGeometry(QtCore.QRect(600, 360, 180, 40))  
        # self.ui.MainWindow.setStyleSheet("background-color: #494a59;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setPointSize(20)
        self.ui.title.setFont(font)
        font.setPointSize(13)
        self.ui.sub_title.setFont(font)
        font.setPointSize(10)
        self.ui.download_mp3.setFont(font)
        self.ui.download_video_btn.setFont(font)
        self.ui.destimation_btn.setFont(font)        
        self.ui.retype.setFont(font)
        







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    alpha = Windows()
    alpha.show()
    sys.exit(app.exec_())
    