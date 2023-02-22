from pymongo import MongoClient
from dotenv import dotenv_values

env = dotenv_values(".env")

mongo = MongoClient('mongo', port=27017,
                    username=env.get("MONGODB_USERNAME"),
                    password=env.get("MONGODB_PASSWORD"))

db = mongo[env.get("MONGODB_DATABASE")]
tweets_table = db['tweets']
