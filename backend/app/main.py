from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.health import router as health_router
from app.routers.users import router as users_router
from app.routers.images import router as images_router

# ─── Lifespan (démarrage / arrêt) ────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestion du cycle de vie de l'application."""
    print("DermaVision AI Backend - demarrage")
    yield
    print("DermaVision AI Backend - arret")


# ─── Application FastAPI ──────────────────────────────────────────────────────
app = FastAPI(
    title="DermaVision AI API",
    description="API backend pour l'application DermaVision AI — detection de maladies cutanees.",
    version="1.0.0",
    lifespan=lifespan,
)

# ─── Middleware CORS ──────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Route racine ─────────────────────────────────────────────────────────────
@app.get("/", tags=["Root"])
def home():
    return {
        "message": "Bienvenue sur DermaVision AI",
        "docs": "/docs",
        "health": "/health",
    }


# ─── Enregistrement des routers ───────────────────────────────────────────────
app.include_router(health_router, tags=["Health"])
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(images_router)