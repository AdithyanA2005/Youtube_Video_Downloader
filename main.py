import os
import sys
import time
from app.settings import data
from pytube import YouTube
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from app.gui import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self, usr_data):
        super().__init__()
        self.data = usr_data
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.download_video_btn.clicked.connect(self.video_download)
        self.ui.download_mp3.clicked.connect(self.audio_download)
        self.ui.destimation_btn.clicked.connect(self.show_downloads)
        self.show()

    def video_download(self):
        self.change_pht("Started Downloading")
        start_time = time.time()
        try:
            self.start_video_download()
        except Exception as e:
            print('error')
        exe_time = time.time() - start_time
        self.change_pht(f"The File was downloaded in {exe_time} seconds")

    def audio_download(self):
        self.change_pht("Started Downloading")
        start_time = time.time()
        try:
            self.start_audio_download()
        except Exception as e:
            print("error")
        exe_time = time.time() - start_time
        self.change_pht(f"The File was downloaded in {exe_time} seconds")

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
        download_destination = f"{self.data['loc']}/videos"
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
        video = url.streams.filter(only_audio=True).first()
        print("40%")
        download_destination = f"{self.data['loc']}/audios"
        print("60%")
        video.download(output_path=download_destination)
        print("80%")
        os.rename(f"{download_destination}/{url.title}.mp4", f"{download_destination}/{url.title}.mp3")
        print("100%")

    def show_downloads(self):
        self.change_pht("OPENING YOUR DOWNLOADED VIDEOS")
        try:
            command = f"{self.data['cmd']}{self.data['loc']}"
            print(command)
            os.system(command)
        except Exception as e:
            print("error opn opening downloads")

    def change_pht(self, text):
        self.ui.entry_field.setText("")
        self.ui.entry_field.setPlaceholderText(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    alpha = Main(data)
    alpha.show()
    sys.exit(app.exec_())
