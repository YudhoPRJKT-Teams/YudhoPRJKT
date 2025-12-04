from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from typing import Any
from .create_log import CreateLog

def DownloadVideo(video_url: str):
  try:
    conf: Any = {
      'format': 'best',
      'outtmpl': 'video.mp4',
      'quiet': True,
      'no_warnings': True,
      'logtostderr': False
    }
    with YoutubeDL(conf) as dl:
      dl.download(video_url)
  except DownloadError as e:
    CreateLog.Error('Catch Error!', str(e))