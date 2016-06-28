# Simple Youtube MP3 Downloader

[![Build Status](https://travis-ci.org/abellosovic/simpleYoutubeMP3Downloader.svg?branch=develop)](https://travis-ci.org/abellosovic/simpleYoutubeMP3Downloader)

# Usage
1. Go to proyect path
2. Build docker image: docker build -tag simpleYoutubeMP3Downloader .
3. Run container: docker run -d -v $(pwd)/app:/opt/cherrypy/app -p [HOST_PORT]:8000 simpleYoutubeMP3Downloader
