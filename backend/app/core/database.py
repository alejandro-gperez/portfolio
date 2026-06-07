"""
Database configuration.

Creates the database engine and session factory used
throughout the application.
"""

from sqlmodel import Session
from sqlmodel import create_engine

from app.core.config import settings

# SQLAlchemy / SQLModel engine.
# Future database models will use this engine.
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
)


def get_session():
    """
    Provide a database session.

    Yields:
        Session: Active database session.
    """
    with Session(engine) as session:
        yield session