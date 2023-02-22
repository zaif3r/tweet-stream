FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install aiohttp async_lru oauthlib pymongo python-dotenv tweepy websockets

CMD [ "python3", "-u", "main.py"]