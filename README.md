# Simple Youtube MP3 Downloader

# Usage
1. Go to proyect path
2. Build docker image: docker build -tag simpleYoutubeMP3Downloader .
3. Run container: docker run -d -v $(pwd)/app:/opt/cherrypy/app -p [HOST_PORT]:8000 simpleYoutubeMP3Downloader
