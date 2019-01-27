FROM python:latest

WORKDIR /app


RUN apt-get update
RUN apt-get -y install sudo
RUN sudo apt-get -y install curl gnupg apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
RUN sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main" > /etc/apt/sources.list.d/microsoft.list'
RUN sudo apt-get update
RUN sudo apt-get -y install -y powershell

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN rm -rf venv
CMD [ "python", "./app.py" ]
