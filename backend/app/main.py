from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers import auth
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Bienvenue sur DermaVision AI 🚀"
    }


app.include_router(health_router)
app.include_router(auth.router)