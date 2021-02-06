# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgba(19, 52, 59, 109);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.sub_title = QtWidgets.QLabel(self.centralwidget)
        self.sub_title.setGeometry(QtCore.QRect(0, 50, 291, 31))
        self.sub_title.setObjectName("sub_title")
        self.entry_field = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_field.setGeometry(QtCore.QRect(20, 130, 761, 71))
        self.entry_field.setObjectName("entry_field")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(530, 230, 101, 26))
        self.checkBox.setObjectName("checkBox")
        self.download_mp3 = QtWidgets.QPushButton(self.centralwidget)
        self.download_mp3.setGeometry(QtCore.QRect(640, 230, 121, 30))
        self.download_mp3.setObjectName("download_mp3")
        self.download_video_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_video_btn.setGeometry(QtCore.QRect(20, 230, 121, 30))
        self.download_video_btn.setObjectName("download_mp3")
        self.download_video_btn.setObjectName("download_video_btn")
        self.destimation_btn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.destimation_btn.setGeometry(QtCore.QRect(30, 360, 172, 41))
        self.destimation_btn.setObjectName("destimation_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adithyan\'s Youtube Video Downloader                                                                                             Fastest Downloader Ever"))
        self.title.setText(_translate("MainWindow", "Adithyans Youtube Video Downloader"))
        self.sub_title.setText(_translate("MainWindow", "Fastest Downloader Ever"))
        self.entry_field.setPlaceholderText(_translate("MainWindow", "ENTER THE URL OF THE YOUTUBE VIDEO THAT YOU WANT TO DOWNLOAD"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.download_mp3.setText(_translate("MainWindow", "Download MP3"))
        self.download_video_btn.setText(_translate("MainWindow", "Download MP4"))
        self.destimation_btn.setText(_translate("MainWindow", "Choose Destination"))



