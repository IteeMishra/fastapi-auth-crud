from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()
uri = os.getenv("URL")

client = MongoClient(uri)

db = client["fastapi"]
collection_name = db["fastapi_collection"]

#user_collection creation
collection_user=db["fastapi_user"]