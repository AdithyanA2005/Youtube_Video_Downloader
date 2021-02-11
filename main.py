import os
import time
from pytube import YouTube
from PyQt5.QtWidgets import *
from app.gui import Ui_MainWindow
from windows.windows_os import Windows
# inp_entry = "https://www.youtube.com/watch?v=sE9oZ4fdb1s"


class Main(QMainWindow):
    def __init__(self, usr_data):
        super().__init__()
        self.data = usr_data
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        vid = "video"
        self.ui.download_video_btn.clicked.connect(self.check_url)
        self.ui.download_mp3.clicked.connect(self.check_url)
        self.ui.clear_entry.clicked.connect(self.clear_it)
        self.ui.destimation_btn.clicked.connect(self.show_downloads)
        windows.load_gui_change(self)
        self.show()

    def video_download(self, inp_entry):
        start_time = time.time()
        try:
            print("0%")
            print(inp_entry)
            print("20%")
            url = YouTube(str(inp_entry))
            print("40%")
            video = url.streams.first()
            print("60%")
            download_destination = f"{self.data['loc']}/videos"
            print("80%")
            video.download(output_path=download_destination)
            print("100%")
            exe_time = time.time() - start_time
            self.change_pht(f"the file was downloaded in {exe_time} seconds")
        except Exception as e:
            print(e)
            self.change_pht("error: please ensure that you have entered a valid url")

    def audio_download(self, inp_entry):
        start_time = time.time()
        try:
            print("0%")
            print(inp_entry)
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
            exe_time = time.time() - start_time
            self.change_pht(f"the file was downloaded in {exe_time} seconds")
        except Exception as e:
            print(e)
            self.change_pht("error: please ensure that you have entered a valid url")

    def show_downloads(self):
        self.change_pht("opening your downloaded videos")
        try:
            command = f"{self.data['cmd']}{self.data['loc']}"
            print(command)
            os.system(command)
            self.change_pht("enter the url")
        except Exception as e:
            print("error opn opening downloads")

    def change_pht(self, text):
        self.ui.entry_field.setText("")
        text = text.upper()
        self.ui.entry_field.setPlaceholderText(text)

    def check_url(self):
        inp_entry = self.ui.entry_field.text()
        sender_button = self.sender()
        key = sender_button.text()
        if inp_entry == "":
            self.change_pht("please enter the url")
        else:
            if "MP4" in key:
                self.video_download(inp_entry)
            elif "MP3" in key:
                self.audio_download(inp_entry)
            else:
                print("Invalid Key")

    def clear_it(self):
        field = self.ui.entry_field
        field.setText("")
        pht = "enter the url of the video that you want to download"
        field.setPlaceholderText(pht.upper())


windows = Windows


if __name__ == '__main__':
    import sys
    from app.settings import data
    from PyQt5 import QtWidgets
    
    app = QtWidgets.QApplication(sys.argv)
    alpha = Main(data)
    alpha.show()
    sys.exit(app.exec_())
