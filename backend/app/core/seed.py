"""
Database seed utilities.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.profile import Profile
from app.models.skill import Skill
from app.models.project import Project
from app.models.feature import Feature
from app.models.event import Event
from app.models.metric import Metric
from app.models.github_metric import GitHubMetric

from app.models.technology import (
    Technology,
)

from app.models.project_technology import (
    ProjectTechnology,
)


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

def seed_events(session: Session) -> None:
    """
    Seed portfolio activity events.
    """

    existing = session.exec(
        select(Event)
    ).first()

    if existing:
        return

    events = [
        Event(
            event_type="PROJECT_CREATED",
            description="Portfolio SaaS project initialized.",
        ),
        Event(
            event_type="DEPLOYMENT",
            description="Initial API deployment completed.",
        ),
        Event(
            event_type="DATABASE_CONNECTED",
            description="PostgreSQL integration completed.",
        ),
        Event(
            event_type="FEATURE_ADDED",
            description="Project-feature relationships implemented.",
        ),
        Event(
            event_type="API_RELEASE",
            description="Version 1 API endpoints released.",
        ),
    ]

    session.add_all(events)

    session.commit()

def seed_metrics(session: Session) -> None:
    """
    Seed dashboard metrics.
    """

    existing = session.exec(
        select(Metric)
    ).first()

    if existing:
        return

    metrics = [
        Metric(
            name="Projects",
            value=1,
        ),
        Metric(
            name="APIs",
            value=6,
        ),
        Metric(
            name="Databases",
            value=1,
        ),
        Metric(
            name="Years Coding",
            value=3,
        ),
    ]

    session.add_all(metrics)

    session.commit()

def seed_github_metrics(
    session: Session,
) -> None:
    """
    Seed GitHub analytics metrics.
    """

    existing = session.exec(
        select(GitHubMetric)
    ).first()

    if existing:
        return

    metrics = [
        GitHubMetric(
            metric_name="Repositories",
            metric_value=12,
        ),
        GitHubMetric(
            metric_name="Commits This Year",
            metric_value=542,
        ),
        GitHubMetric(
            metric_name="Pull Requests",
            metric_value=36,
        ),
        GitHubMetric(
            metric_name="Stars",
            metric_value=18,
        ),
    ]

    session.add_all(metrics)

    session.commit()

def seed_technologies(
    session: Session,
) -> None:
    """
    Seed technologies.
    """

    existing = session.exec(
        select(Technology)
    ).first()

    if existing:
        return

    technologies = [
        Technology(
            name="FastAPI",
            category="Backend",
        ),
        Technology(
            name="PostgreSQL",
            category="Database",
        ),
        Technology(
            name="Docker",
            category="DevOps",
        ),
        Technology(
            name="React",
            category="Frontend",
        ),
    ]

    session.add_all(
        technologies
    )

    session.commit()

def seed_project_technologies(
    session: Session,
) -> None:
    """
    Seed project technology relations.
    """

    existing = session.exec(
        select(ProjectTechnology)
    ).first()

    if existing:
        return

    project = session.exec(
        select(Project)
    ).first()

    technologies = session.exec(
        select(Technology)
    ).all()

    relations = [
        ProjectTechnology(
            project_id=project.id,
            technology_id=tech.id,
        )
        for tech in technologies
    ]

    session.add_all(relations)

    session.commit()