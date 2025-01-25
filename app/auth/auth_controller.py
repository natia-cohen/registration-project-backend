from fastapi import HTTPException
from app.auth.auth_model import UserSignup, UserLogin, ForgotPasswordRequest
from app.auth.auth_service import create_user, get_user_by_email, verify_password, create_reset_token
from app.auth.mail_service import send_reset_email

async def login(user: UserLogin):
    found_user = get_user_by_email(user.email)
    if not found_user or not verify_password(user.password, found_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"id": str(found_user["_id"]), "email": found_user["email"]}


async def signup(user: UserSignup):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    user_data = {"email": user.email, "password": user.password}

    user_id = create_user(user_data)
    return {"id": user_id, "email": user.email}

async def forgot_password(email: str):
    user = get_user_by_email(email)
    print(email, user)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reset_token = create_reset_token(email)
    await send_reset_email(email, reset_token)

    return {"message": "Reset password email sent successfully"}
