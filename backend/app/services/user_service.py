from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import hash_password


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