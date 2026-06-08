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
from app.models.skill import Skill
from app.models.project import Project
from app.models.feature import Feature
from app.models.event import Event

from sqlmodel import Session

from app.core.seed import (
    seed_profile,
    seed_skills,
    seed_projects,
    seed_events,
)

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
        seed_skills(session)
        seed_projects(session)
        seed_events(session)


def get_session():
    """
    Provide a database session.
    """
    with Session(engine) as session:
        yield session