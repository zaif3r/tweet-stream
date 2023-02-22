import asyncio
import json

from tweepy.asynchronous import AsyncStreamingClient
from pprint import pprint

from db import tweets_table


class PubSub:
    def __init__(self):
        self.waiter = asyncio.Future()

    def publish(self, value):
        waiter, self.waiter = self.waiter, asyncio.Future()
        waiter.set_result((value, self.waiter))

    async def subscribe(self):
        waiter = self.waiter
        while True:
            value, waiter = await waiter
            yield value

    __aiter__ = subscribe


class StreamClient(AsyncStreamingClient):
    def __init__(self, bearer_token):
        super().__init__(bearer_token)
        self.pubsub = PubSub()

    async def on_data(self, data):
        dataObj = json.loads(str(data, 'utf-8'))
        if dataObj.get('data'):
            tweets_table.insert_one(dataObj)
            self.pubsub.publish(data)
        else:
            pprint("[stream client error]: on_data", dataObj)
            self.disconnect()

    async def on_connection_error(self):
        print("[stream client error]: on_connection_error")
        self.disconnect()

    async def on_error(self, status):
        pprint("[stream client error]: on_error", status)
        self.disconnect()
