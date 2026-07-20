import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ─── URL de la base de données ────────────────────────────────────────────────
# Priorité : variable d'environnement DATABASE_URL, sinon valeur par défaut.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5433/dermavision_ai"
)

# ─── Moteur SQLAlchemy ────────────────────────────────────────────────────────
engine = create_engine(DATABASE_URL)

# ─── Session factory ──────────────────────────────────────────────────────────
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ─── Base déclarative ─────────────────────────────────────────────────────────
Base = declarative_base()


# ─── Dépendance FastAPI ───────────────────────────────────────────────────────
def get_db():
    """Fournit une session de base de données et la ferme après usage."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()