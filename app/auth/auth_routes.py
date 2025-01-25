from fastapi import APIRouter
from app.auth.auth_model import UserSignup, UserLogin,  ForgotPasswordRequest
from app.auth.auth_controller import login, signup, forgot_password

router = APIRouter()

@router.post("/auth/login")
async def login_route(user: UserLogin):
    return await login(user)

@router.post("/auth/signup")
async def signup_route(user: UserSignup):
    return await signup(user)

@router.post("/auth/forgot-password")
async def forgot_password_route(email: ForgotPasswordRequest):
    return await forgot_password(email.email)
