from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    """Données requises pour l'inscription d'un utilisateur."""
    full_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Données retournées après création ou consultation d'un utilisateur."""
    id: int
    full_name: str
    email: EmailStr
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    """Données modifiables du profil utilisateur."""

    full_name: Optional[str] = None
    email: Optional[EmailStr] = None


class PasswordUpdate(BaseModel):
    current_password: str
    new_password: str