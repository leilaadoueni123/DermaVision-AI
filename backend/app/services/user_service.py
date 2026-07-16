from sqlalchemy.orm import Session

from app.models.user import User
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def create_user(
    db: Session,
    full_name: str,
    email: str,
    password: str
):

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