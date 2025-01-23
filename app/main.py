from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.users import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, tags=["Users"])

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
