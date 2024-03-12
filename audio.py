from pytube import YouTube
from datetime import datetime
import os
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

from application import YoutubeApp

class YoutubeVideo:
    def __init__(self, channel_name="@yutinghao"):
        self.video_id = YoutubeApp().get_latest_video_id(channel_name)
        self.file_name = None
        self.file_path = None

    def get_video_name(self):
        if self.file_name:
            print(f'current video file name: {self.file_name}')
        elif not self.file_name:
            print('Execute "download_video" method to assign file_name to this object.')
        return self.file_name
    
    def get_video_path(self):
        if self.file_path:
            print(f'current video file path: {self.file_path}')
        elif not self.file_path:
            print('Execute "download_video" method to assign file_path to this object.')
        return self.file_path

    def download_video(self):
        yt_video = YouTube(f'https://www.youtube.com/watch?v={self.video_id}')
        self.file_name = f'{yt_video.author}_{datetime.now().strftime("%Y-%m-%d")}'
        self.file_path = f'{os.getcwd()}/data/{self.file_name}.mkv'
        audio_file = yt_video.streams.filter(
            only_audio=True, 
            ).first().download(filename=self.file_path)
        print(f"successfully downloaded {audio_file}.")