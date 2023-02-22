import asyncio

from dotenv import dotenv_values

from client import StreamClient
from stream import start_stream

env = dotenv_values(".env")


async def main():
    client = StreamClient(env.get("TWITTER_BEARER_TOKEN"))
    await start_stream(client)
    
if __name__ == "__main__":
    asyncio.run(main())
