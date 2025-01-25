import os
from dotenv import load_dotenv

from app.database import users_collection
from passlib.context import CryptContext
from bson import ObjectId
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import jwt


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user):
    user["password"] = hash_password(user["password"]) 
    result = users_collection.insert_one(user) 
    return str(result.inserted_id)

def get_user_by_email(email):
    return users_collection.find_one({"email": email})

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def create_reset_token(email):
    expiration = datetime.utcnow() + timedelta(hours=1)  
    payload = {"sub": email, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)