from fastapi import APIRouter


router = APIRouter(
    prefix="/images",
    tags=["Images"]
)
@router.post("/upload")
def upload_image():
    """
    Upload d'une image dermatologique.
    """
    return {
        "message": "Image reçue avec succès"
    }