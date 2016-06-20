from __future__ import unicode_literals
import youtube_dl


class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class Mp3Downloader(object):

    ydl_opts = {}

    def __init__(self, download_folder):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': Logger(),
            'outtmpl': '{0}/%(title)s.%(ext)s'.format(download_folder)
        }


    def download(self, url):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])
