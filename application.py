import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
load_dotenv()

class YoutubeApp:
    def __init__(self):
        self.yt_key = os.getenv("yt_api_key")

    def get_latest_video_id(self, channel_name):  # in the tail of channel's url
        gcp_yt = build('youtube', 'v3', developerKey=self.yt_key)
        channel_id = os.getenv(f"channel_id_{channel_name.strip('@')}")

        if channel_id:
            try:
                latest_video = gcp_yt.search().list(
                    part="snippet",
                    channelId=channel_id,
                    order="date"
                ).execute()
                video_id = latest_video['items'][0]['id']['videoId']
                video_title = latest_video['items'][0]['snippet']['title']
                print("Latest Video ID:", video_id)
                print("Latest Video Title:", video_title)

                return video_id
            
            except Exception as e:
                raise RuntimeError(e)
        
        elif not channel_id:
            raise ValueError(f'This channel_id is not found in .env file. Please go to channel description page https://www.youtube.com/{channel_name}, press ctl + u and search for "channl_id". Add it in the .env file.')