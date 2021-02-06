import os

from pytube import YouTube
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from app.gui import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.download_video_btn.clicked.connect(self.start_video_download)
        self.ui.download_mp3.clicked.connect(self.start_audio_download)
        self.show()

    def start_video_download(self):
        print("0%")
        inp_entry = self.ui.entry_field.text()
        print(inp_entry)
        # inp_entry = "https://www.youtube.com/watch?v=sE9oZ4fdb1s"
        print("20%")
        url = YouTube(str(inp_entry))
        print("40%")
        video = url.streams.first()
        print("60%")
        download_destination = "yt/videos"
        print("80%")
        video.download(output_path=download_destination)
        print("100%")

    def start_audio_download(self):
        print("0%")
        inp_entry = self.ui.entry_field.text()
        print(inp_entry)
        # inp_entry = "https://www.youtube.com/watch?v=sE9oZ4fdb1s"
        print("10%")
        url = YouTube(str(inp_entry))
        print("20%")
        video = url.streams.filter(only_audio = True).first()
        print("40%")
        download_destination = "yt/audios"
        print("60%")
        video.download(output_path=download_destination)
        print("80%")
        os.rename(f"yt/audios/{url.title}.mp4", f"yt/audios/{url.title}.mp3")
        print("100%")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    alpha = Main()
    alpha.show()
    sys.exit(app.exec_())
