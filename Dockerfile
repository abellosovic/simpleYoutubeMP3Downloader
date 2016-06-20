FROM ubuntu:xenial

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libav-tools

WORKDIR /opt/cherrypy/

# Install python dependencies
RUN apt-get install -y python-pip && \
  pip install pip --upgrade && \
  pip install virtualenv

RUN mkdir env && virtualenv env

COPY requirements.txt /tmp/
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN source /opt/cherrypy/env/bin/activate && \
  pip install -r /tmp/requirements.txt

VOLUME app/
EXPOSE 8000

CMD source /opt/cherrypy/env/bin/activate && python app/app.py
