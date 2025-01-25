from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.auth_routes import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=["Auth"])

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
