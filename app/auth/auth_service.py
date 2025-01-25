from app.database import users_collection
from passlib.context import CryptContext
from bson import ObjectId
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user_dict["password"])  
    result = users_collection.insert_one(user_dict)
    return str(result.inserted_id)

def get_user_by_email(email):
    return users_collection.find_one({"email": email})

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)
