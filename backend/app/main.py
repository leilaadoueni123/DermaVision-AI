from fastapi import FastAPI
from backend.app.routers.health import router as health_router

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Bienvenue sur DermaVision AI 🚀"
    }


app.include_router(health_router)