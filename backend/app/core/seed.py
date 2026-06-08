"""
Database seed utilities.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.profile import Profile
from app.models.skill import Skill
from app.models.project import Project
from app.models.feature import Feature


def seed_profile(session: Session) -> None:
    """
    Seed initial profile data.
    """

    existing_profile = session.exec(
        select(Profile)
    ).first()

    if existing_profile:
        return

    profile = Profile(
        name="Alejandro Perez",
        title="Backend Engineer",
        bio="Building APIs, data pipelines and scalable systems.",
        github_url="https://github.com/your-user",
        linkedin_url="https://linkedin.com/in/your-user",
        email="your-email@example.com",
        location="Guatemala",
        profile_image_url="https://example.com/profile.jpg",
    )

    session.add(profile)
    session.commit()

def seed_skills(session: Session) -> None:
    """
    Seed portfolio skills.
    """

    existing = session.exec(
        select(Skill)
    ).first()

    if existing:
        return

    skills = [
        Skill(
            name="FastAPI",
            category="Backend",
            level=5,
        ),
        Skill(
            name="PostgreSQL",
            category="Database",
            level=4,
        ),
        Skill(
            name="Docker",
            category="DevOps",
            level=4,
        ),
        Skill(
            name="Pandas",
            category="Data",
            level=4,
        ),
    ]

    session.add_all(skills)

    session.commit()

def seed_projects(session: Session) -> None:
    """
    Seed featured projects.
    """

    existing = session.exec(
        select(Project)
    ).first()

    if existing:
        return

    project = Project(
        name="Portfolio SaaS",
        description=(
            "Backend-focused portfolio platform."
        ),
        status="In Progress",
        featured=True,
        github_url=(
            "https://github.com/your-user/portfolio-saas"
        ),
    )

    session.add(project)

    session.commit()

    session.refresh(project)

    features = [
        Feature(
            project_id=project.id,
            name="REST API",
        ),
        Feature(
            project_id=project.id,
            name="GitHub Analytics",
        ),
        Feature(
            project_id=project.id,
            name="Event Tracking",
        ),
        Feature(
            project_id=project.id,
            name="Observability Dashboard",
        ),
    ]

    session.add_all(features)

    session.commit()