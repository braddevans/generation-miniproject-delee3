#!/bin/sh

docker kill mini-project && docker rm mini-project

# docker run a container from an image
# Interactive with tty
# Add in Volume Bind from local filesystem to container folder
# working directory /usr/src/app
# image: python:3.10
# run command in container: /bin/bash -c "pip install -r requirements.txt; python main.py"
docker run \
    -it \
    --name=mini-project \
    -v /generation/mini-project/:/usr/src/app/ \
    -w /usr/src/app \
    python:3.10 \
    /bin/bash -c "pip install -r requirements.txt; python main.py"