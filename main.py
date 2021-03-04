import os
import sys
import time
import platform
from pytube import YouTube as YT
from app.settings import data
# inp_entry = "https://www.youtube.com/watch?v=sE9oZ4fdb1s"


class Main():
    def __init__(self, cli_values):
        super().__init__()
        self.start_app()


    def start_app(self):
        try:
            self.video_url = sys.argv[1]
        except Exception as e:
            self.video_url = ""
        try:
            self.video_name = sys.argv[2]
        except Exception as e:
            self.video_name = ""

        self.data = data
        
        if self.video_name == "":
            self.video_download(self.video_url, self.video_name)

        elif self.video_name == "mp4":
            self.video_download(self.video_url, self.video_name)

        elif self.video_name == "video":
            self.video_download(self.video_url, self.video_name)

        elif self.video_name == "mp3":
            self.audio_download(self.video_url, self.video_name)

        elif self.video_name == "audio":
            self.audio_download(self.video_url, self.video_name)

        else:
            self.video_download(self.video_url, self.video_name)
        
        

    def video_download(self, url, name):
        try:
            start_time = time.time()
            url_start = "https://www.youtube.com/watch?v="

            if url_start in url:
                video_url = str(url)
                print("0%")
                print(f"The url you have entered is: \n-> {url}\nThe Name of the Video is: \n->{name}")
                print("20%")
                url = YT(video_url) 
                print("40%")
                video = url.streams.first()
                print("50%")
                download_destination = self.get_location()
                download_destination = f"{download_destination}videos"
                print("80%")
                video.download(output_path=download_destination)
                print("100%")
                print(f"The video has been downloaded in the location {download_destination}")
                exe_time = time.time() - start_time
                print(f"Process completed in {exe_time}")
                self.show_downloads(download_destination)

            else:
                print("This is not a valid URL")

        except Exception as e:
            print("Stopped in video_download function because: ")
            print(e)


    def audio_download(self, url, name):
        start_time = time.time()
        try:
            video_url = str(url)
            print("0%")
            print(f"The url you have entered is: \n-> {url}\nThe Name of the Video is: \n->{name}")
            print("20%")
            url = YT(video_url)
            print("30%")
            video = url.streams.filter(only_audio=True).first()
            print("40%")
            download_destination = self.get_location()
            download_destination = f"{download_destination}audio"
            print("60%")
            video.download(output_path=download_destination)
            print("80%")
            os.rename(f"{download_destination}/{url.title}.mp4", f"{download_destination}/{url.title}.mp3")
            print("100%")
            print(f"The audio file has been downloaded in the location {download_destination}")
            exe_time = time.time() - start_time
            print(f"Process completed in {exe_time}")
            self.show_downloads(download_destination)

        except Exception as e:
            print("Stopped in audio_download function because: ")
            print(e)


    def get_location(self):
        self.operating_system = platform.system()
        yt_folder = data["loc"]

        if self.operating_system == "Windows":
            download_destination = f"{yt_folder}\\"
        elif self.operating_system == "Linux":
            download_destination = f"{yt_folder}\\"
            download_destination = download_destination.replace("\\", "/")
        else:
            download_destination = "Youtube_Video_Downloader"
        return download_destination


    def show_downloads(self, download_destination):
        print("PRESS '1' TO SHOW THE DOWNLOAD FOLDER \nPRESS '2' TO EXIT THE PROGRAM")
        show_bool = str(input("Enter Your Option(1, 2): "))
        if show_bool == "1": 
            try:
                os.system(f"explorer {download_destination}")

            except:
                os.system(f"xdg-open {download_destination}")

        elif show_bool == "2":
            sys.exit("Bye sir")

        else:
            sys.exit("Bye sir")


if __name__ == '__main__':
    alpha = Main(sys.argv)

