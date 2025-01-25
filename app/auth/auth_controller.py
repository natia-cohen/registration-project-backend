from fastapi import HTTPException
from app.auth.auth_model import UserSignup, UserLogin
from app.auth.auth_service import create_user, get_user_by_email, verify_password

async def login(user: UserLogin):
    found_user = get_user_by_email(user.email)
    if not found_user or not verify_password(user.password, found_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"id": str(found_user["_id"]), "email": found_user["email"]}

async def signup(user: UserSignup):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    user_id = create_user(user)
    return {"id": user_id, "email": user.email}
