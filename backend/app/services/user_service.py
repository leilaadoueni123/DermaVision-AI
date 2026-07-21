from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserUpdate
from fastapi import HTTPException, status

def create_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
) -> User:
    """
    Crée un nouvel utilisateur dans la base de données.
    Le mot de passe est haché avant stockage.
    """
    hashed_password = hash_password(password)

    user = User(
        full_name=full_name,
        email=email,
        password_hash=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db: Session, email: str):
    """Récupère un utilisateur par son email."""
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    """Récupère un utilisateur par son ID."""
    return db.query(User).filter(User.id == user_id).first()

def update_user(
    db: Session,
    user: User,
    user_data: UserUpdate
):
    """
    Met à jour les informations du profil utilisateur.
    """

    if user_data.full_name is not None:
        user.full_name = user_data.full_name

    if user_data.email is not None:
        user.email = user_data.email


    db.commit()

    db.refresh(user)

    return user

from app.core.security import (
    verify_password,
    hash_password
)

def change_password(
    db,
    user,
    current_password: str,
    new_password: str
):
    """
    Change le mot de passe d'un utilisateur.
    """

    # Vérifier l'ancien mot de passe
    if not verify_password(
        current_password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ancien mot de passe incorrect."
        )


    # Hasher le nouveau mot de passe
    user.password_hash = hash_password(
        new_password
    )


    # Sauvegarder
    db.commit()

    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user: User
):
    """
    Supprime un utilisateur de la base de données.
    """

    db.delete(user)
    db.commit()

    return True