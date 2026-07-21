from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.user import User
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.user import UserUpdate, UserResponse
from app.services.user_service import update_user
from app.database import get_db
from app.schemas.user import PasswordUpdate
from app.services.user_service import change_password
from app.services.user_service import delete_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    """
    Retourne le profil de l'utilisateur connecté.
    """

    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "created_at": current_user.created_at
    }
@router.put("/me", response_model=UserResponse)
def update_my_profile(
    user_data: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Modifier le profil de l'utilisateur connecté.
    """

    updated_user = update_user(
        db,
        current_user,
        user_data
    )

    return updated_user

@router.put("/password")
def update_password(
    password_data: PasswordUpdate,
    current_user: User = Depends(get_current_user),
    db = Depends(get_db)
):
    """
    Permet à l'utilisateur connecté de changer son mot de passe.
    """

    change_password(
        db,
        current_user,
        password_data.current_password,
        password_data.new_password
    )


    return {
        "message": "Mot de passe modifié avec succès."
    }

@router.delete("/me")
def delete_my_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Supprime le compte de l'utilisateur connecté.
    """

    delete_user(
        db,
        current_user
    )

    return {
        "message": "Compte supprimé avec succès"
    }