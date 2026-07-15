from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Bienvenue sur DermaVision AI 🚀"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "DermaVision AI Backend is running"
    }