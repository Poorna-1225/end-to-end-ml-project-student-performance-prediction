from python:3.8-slim-buster
workdir /app
copy . /app

run apt update -y && apt isntall awscli -y


run pip install -r requirements.txt
cmd['python3','app.py']