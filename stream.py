import websockets
import functools

from dotenv import dotenv_values

env = dotenv_values(".env")

port = int(env.get("WEBSOCKET_PORT"))

filter_config = {
    "expansions": "author_id,entities.mentions.username,geo.place_id",
    "user.fields": "name,username,location,profile_image_url",
    "tweet.fields": "id,text,created_at,public_metrics,entities,author_id",
}


async def stream_handler(websocket, client=None):
    print("[stream handler]: listening", websocket.remote_address)
    try:
        async for message in client.pubsub:
            await websocket.send(message)
    except Exception as e:
        print("[stream handler error]: ", e)


async def start_stream(client):
    try:
        async with websockets.serve(functools.partial(stream_handler, client=client), "", port):
            print("[twitter stream]: filter config", filter_config)

            print(f"[twitter stream]: started at port {port}")
            try:
                await client.filter(expansions=filter_config["expansions"],
                                    user_fields=filter_config["user.fields"],
                                    tweet_fields=filter_config["tweet.fields"])
            except Exception as e:
                print("[twitter stream error]: ", e)
                client.disconnect()
    except Exception as e:
        print("[twitter stream error]: ", e)
        client.disconnect()
