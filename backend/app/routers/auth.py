from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserRegister, UserResponse
from app.schemas.auth import TokenResponse
from app.services.user_service import create_user, get_user_by_email
from app.services.auth_service import login_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Inscription d'un nouvel utilisateur"
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    """
    Crée un compte utilisateur.
    """

    existing = get_user_by_email(db, user.email)

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Un compte avec cet email existe déjà."
        )

    new_user = create_user(
        db,
        user.full_name,
        user.email,
        user.password
    )

    return new_user



@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Connexion et obtention du token JWT"
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authentifie un utilisateur et retourne un JWT.

    username correspond à l'email utilisateur.
    """

    token = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect.",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )

    return token