from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient("127.0.0.1", 27017)
    db = client["TaskMate"]
    # Test the connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
