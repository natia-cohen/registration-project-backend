from fastapi import APIRouter
from app.auth.auth_model import UserSignup, UserLogin
from app.auth.auth_controller import login, signup

router = APIRouter()

@router.post("/auth/login")
async def login_route(user: UserLogin):
    return await login(user)

@router.post("/auth/signup")
async def signup_route(user: UserSignup):
    return await signup(user)
