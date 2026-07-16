from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserRegister
from app.services.user_service import create_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    new_user = create_user(
        db,
        user.full_name,
        user.email,
        user.password
    )

    return {
        "id": new_user.id,
        "full_name": new_user.full_name,
        "email": new_user.email
    }