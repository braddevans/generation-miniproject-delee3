@echo on

:: docker run a container from an image
:: Interactive with tty
:: Set name to: Mini-Project
:: Add in Volume Bind from local filesystem to container folder
:: note for the above comment: "%~dp0" pulls in the current directory and path
:: working directory /usr/src/app
:: image: python:3.10
:: run command in container: /bin/bash -c "pip install -r requirements.txt; python main.py"

docker kill mini-project
docker rm mini-project

docker run^
 -it^
 --name=Mini-Project^
 -v %~dp0:/usr/src/app/^
 -w /usr/src/app^
 python:3.10^
 /bin/bash -c "pip install -r requirements.txt; python main.py"