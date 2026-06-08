"""
Database configuration.

Creates the database engine and session factory used
throughout the application.
"""

from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine

from app.core.config import settings

# Import models so SQLModel registers them.
from app.models.profile import Profile

from sqlmodel import Session

from app.core.seed import seed_profile

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
)


def create_db_and_tables() -> None:
    """
    Create all registered database tables.
    """
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        seed_profile(session)


def get_session():
    """
    Provide a database session.
    """
    with Session(engine) as session:
        yield session