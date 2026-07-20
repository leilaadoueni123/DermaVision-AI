from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Vérification de l'état du serveur")
def health_check():
    """Retourne l'état de santé de l'API DermaVision AI."""
    return {
        "status": "ok",
        "message": "DermaVision AI Backend is running",
        "version": "1.0.0"
    }