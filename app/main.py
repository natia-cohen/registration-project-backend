from fastapi import FastAPI
from app.routes.users import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, tags=["Users"])

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
