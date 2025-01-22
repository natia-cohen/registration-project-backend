from fastapi import APIRouter, HTTPException
from app.models import UserSignup, UserLogin
from app.services.user_service import create_user, get_users, update_user, delete_user, get_user_by_email
from bson import ObjectId

router = APIRouter(prefix="/api")


@router.post("/auth/login")
def login(user: UserLogin):
    found_user = get_user_by_email(user.email, user.password)
    if not found_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"id": str(found_user["_id"]), "email": found_user["email"]}


@router.post("/auth/signup")
def signup(user: UserSignup):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    user_id = create_user(user)
    return {"id": user_id, "email": user.email}


@router.get("/user")
def read():
    return get_users()


@router.put("/user/{user_id}")
def update(user_id: str, user: UserSignup):
    if not update_user(user_id, user):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}


@router.delete("/user/{user_id}")
def delete(user_id: str):
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
