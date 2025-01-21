from fastapi import APIRouter, HTTPException
from app.models import User
from app.services.user_service import create_user, get_users, update_user, delete_user
from app.database import users_collection
from bson import ObjectId

router = APIRouter()

@router.post("/")
def create(user: User):
    user_id = create_user(user)
    return {"id": user_id}

@router.get("/")
def read():
    return get_users()

@router.put("/{user_id}")
def update(user_id: str, user: User):
    if not update_user(user_id, user):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
def delete(user_id: str):
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
