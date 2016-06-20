# Simple Youtube MP3 Downloader

# Usage
1. Go to proyect path
2. Build docker image
    ```bash
    docker build -tag simpleYoutubeMP3Downloader .
    ```
3. Run container
    ```bash
    docker run -d -v $(pwd)/app:/opt/cherrypy/app -p [HOST_PORT]:8000 cherrypy
    ```
