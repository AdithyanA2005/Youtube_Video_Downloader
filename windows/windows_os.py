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
        self.ui.download_mp3.setStyleSheet("background-color: #17a2b8; color :white;")
        self.ui.download_mp3.setGeometry(QtCore.QRect(640, 260, 140, 40))            
        self.ui.download_video_btn.setStyleSheet("background-color: #17a2b8; color :white")   
        self.ui.download_video_btn.setGeometry(QtCore.QRect(20, 260, 140, 40)) 
        self.ui.title.setStyleSheet(" color: #6c757d;")     
        self.ui.sub_title.setStyleSheet("color: #2a5c49")
        self.ui.sub_title.setGeometry(QtCore.QRect(50, 40, 340, 40))
        self.ui.entry_field.setStyleSheet("color:white;")
        self.ui.clear_entry.setGeometry(QtCore.QRect(600, 360, 180, 40))  
        self.ui.clear_entry.setStyleSheet("background-color: #6c757d; color: white;")
        self.ui.destimation_btn.setStyleSheet("background-color: #6c757d; color: white;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setPointSize(20)
        self.ui.title.setFont(font)
        font.setPointSize(13)
        self.ui.sub_title.setFont(font)
        font.setPointSize(10)
    