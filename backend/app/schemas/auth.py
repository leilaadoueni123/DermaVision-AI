from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """
    Données nécessaires pour connecter un utilisateur.
    """

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """
    Réponse envoyée après une connexion réussie.
    """

    access_token: str
    token_type: str = "bearer"