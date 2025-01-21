from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)


db = client["registration_db"]
users_collection = db["users"]
