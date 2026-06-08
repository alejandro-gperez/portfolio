"""
Database seed utilities.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.profile import Profile


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