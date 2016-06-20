import os

import cherrypy
from cherrypy.lib.static import serve_file
from jinja2 import Environment, FileSystemLoader
from mp3downloader import Mp3Downloader

env = Environment(loader=FileSystemLoader('app/templates'))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(PROJECT_ROOT, 'music')):
    os.makedirs(os.path.join(PROJECT_ROOT, 'music'))

DOWNLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'music')

class Root(object):

    @cherrypy.expose
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(mp3_files=get_music())

    @cherrypy.expose
    def download(self, url):
        download_ok = False
        try:
            Mp3Downloader_ins = Mp3Downloader(DOWNLOAD_FOLDER)
            Mp3Downloader_ins.download(url)
            download_ok = True
        except Exception as e:
            cherrypy.log("Fallo la descarga", traceback=True)
        tmpl = env.get_template('index.html')
        return tmpl.render(mp3_files=get_music(), download_ok=download_ok)

    @cherrypy.expose
    def downloadmp3(self, filepath):
        return serve_file(filepath, "application/x-download", "attachment")

    @cherrypy.expose
    def path(self):
        return DOWNLOAD_FOLDER


def get_music():
    mp3_files = []
    for filename in os.listdir(DOWNLOAD_FOLDER):
        if filename.endswith('.mp3'):
            mp3_files.append(filename.decode('utf-8'))
    return mp3_files

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',})
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '8000')),})
    cherrypy.quickstart(Root(), '/', 'app/app.config')
