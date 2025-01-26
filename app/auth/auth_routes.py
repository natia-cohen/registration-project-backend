from fastapi import APIRouter
from app.auth.auth_model import UserSignup, UserLogin,  ForgotPasswordRequest, ResetPasswordRequest
from app.auth.auth_controller import login, signup, forgot_password, reset_password

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


@router.post("/auth/reset-password")
async def reset_password_route(request: ResetPasswordRequest):
    return await reset_password(request.token, request.new_password)
 