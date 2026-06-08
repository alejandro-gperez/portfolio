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
    name="Alejandro Gabriel Pérez Muñoz",
    title="Backend Developer & Data Engineering Enthusiast",
    bio=(
        "Building backend systems, data pipelines, "
        "and event-driven applications."
    ),
    github_url="https://github.com/alejandro-gperez",
    linkedin_url="https://www.linkedin.com/in/alejandro-gabriel-pérez-muñoz-3b664a394",
    email="alejandrogpmunoz@gmail.com",
    location="Guatemala",
    profile_image_url=None, ##CAMBIAR
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
        # Backend
        Skill(
            name="Python",
            category="Backend",
            level=5,
        ),
        Skill(
            name="Java",
            category="Backend",
            level=4,
        ),
        Skill(
            name="Go",
            category="Backend",
            level=4,
        ),
        Skill(
            name="TypeScript",
            category="Backend",
            level=4,
        ),

        # Databases
        Skill(
            name="PostgreSQL",
            category="Database",
            level=4,
        ),
        Skill(
            name="Neo4j",
            category="Database",
            level=4,
        ),
        Skill(
            name="Supabase",
            category="Database",
            level=4,
        ),

        # Data
        Skill(
            name="Celonis",
            category="Data",
            level=4,
        ),
        Skill(
            name="Process Mining",
            category="Data",
            level=4,
        ),
        Skill(
            name="Data Integration",
            category="Data",
            level=4,
        ),

        # DevOps
        Skill(
            name="Docker",
            category="DevOps",
            level=4,
        ),
        Skill(
            name="RabbitMQ",
            category="DevOps",
            level=4,
        ),
        Skill(
            name="Git",
            category="DevOps",
            level=4,
        ),

        # Frameworks
        Skill(
            name="FastAPI",
            category="Frameworks",
            level=5,
        ),
        Skill(
            name="Spring Boot",
            category="Frameworks",
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

    projects = [
        Project(
            name="Intent Classification System",
            description=(
                "Event-driven architecture featuring DistilBERT fine-tuning "
                "with RabbitMQ workers and dockerized services for "
                "asynchronous processing."
            ),
            status="Completed",
            featured=True,
            github_url=(
                "https://github.com/alejandro-gperez/"
                "intent-classification-with-transformers"
            ),
        ),
        Project(
            name="Series Recommendation System",
            description=(
                "Graph-based recommendation system with a REST API "
                "delivering personalized suggestions optimized "
                "through Cypher queries."
            ),
            status="Completed",
            featured=True,
            github_url=(
                "https://github.com/esteban-dlp/recomendaciones"
            ),
        ),
        Project(
            name="WhereNow",
            description=(
                "Mobile application built with MVVM architecture, "
                "Firebase authentication, real-time synchronization "
                "and social features."
            ),
            status="Completed",
            featured=True,
            github_url=(
                "https://github.com/mariale-sierra/Wherenow"
            ),
        ),
        Project(
            name="Portfolio SaaS",
            description=(
                "Backend-focused portfolio platform powered by "
                "FastAPI and PostgreSQL featuring event tracking, "
                "analytics and API documentation."
            ),
            status="In Progress",
            featured=True,
            github_url=(
                "https://github.com/alejandro-gperez/portfolio"
            ),
        ),
    ]

    session.add_all(projects)

    session.commit()

    projects_by_name = {
        project.name: project
        for project in session.exec(
            select(Project)
        ).all()
    }

    features = [
        # Intent Classification System
        Feature(
            project_id=projects_by_name[
                "Intent Classification System"
            ].id,
            name="DistilBERT Fine-Tuning",
        ),
        Feature(
            project_id=projects_by_name[
                "Intent Classification System"
            ].id,
            name="Event-Driven Architecture",
        ),
        Feature(
            project_id=projects_by_name[
                "Intent Classification System"
            ].id,
            name="RabbitMQ Workers",
        ),
        Feature(
            project_id=projects_by_name[
                "Intent Classification System"
            ].id,
            name="Asynchronous Processing",
        ),
        Feature(
            project_id=projects_by_name[
                "Intent Classification System"
            ].id,
            name="Dockerized Services",
        ),

        # Series Recommendation System
        Feature(
            project_id=projects_by_name[
                "Series Recommendation System"
            ].id,
            name="Graph-Based Recommendations",
        ),
        Feature(
            project_id=projects_by_name[
                "Series Recommendation System"
            ].id,
            name="REST API",
        ),
        Feature(
            project_id=projects_by_name[
                "Series Recommendation System"
            ].id,
            name="Cypher Query Optimization",
        ),
        Feature(
            project_id=projects_by_name[
                "Series Recommendation System"
            ].id,
            name="Personalized Suggestions",
        ),

        # WhereNow
        Feature(
            project_id=projects_by_name[
                "WhereNow"
            ].id,
            name="MVVM Architecture",
        ),
        Feature(
            project_id=projects_by_name[
                "WhereNow"
            ].id,
            name="Firebase Authentication",
        ),
        Feature(
            project_id=projects_by_name[
                "WhereNow"
            ].id,
            name="Real-Time Data",
        ),
        Feature(
            project_id=projects_by_name[
                "WhereNow"
            ].id,
            name="Social Features",
        ),

        # Portfolio SaaS
        Feature(
            project_id=projects_by_name[
                "Portfolio SaaS"
            ].id,
            name="FastAPI Backend",
        ),
        Feature(
            project_id=projects_by_name[
                "Portfolio SaaS"
            ].id,
            name="PostgreSQL",
        ),
        Feature(
            project_id=projects_by_name[
                "Portfolio SaaS"
            ].id,
            name="Swagger Documentation",
        ),
        Feature(
            project_id=projects_by_name[
                "Portfolio SaaS"
            ].id,
            name="Event Tracking",
        ),
        Feature(
            project_id=projects_by_name[
                "Portfolio SaaS"
            ].id,
            name="GitHub Analytics",
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
        event_type="INTERNSHIP_STARTED",
        description=(
            "Started Data Analyst & Process Mining Internship "
            "at Embotelladora La Mariposa."
        ),
    ),
    Event(
        event_type="TEACHING_ASSISTANT",
        description=(
            "Began working as Teaching Assistant for "
            "Algorithms and Programming."
        ),
    ),
    Event(
        event_type="PROJECT_COMPLETED",
        description=(
            "Developed Intent Classification System "
            "using DistilBERT and RabbitMQ."
        ),
    ),
    Event(
        event_type="PROJECT_COMPLETED",
        description=(
            "Built Graph-Based Series Recommendation System."
        ),
    ),
    Event(
        event_type="PROJECT_CREATED",
        description=(
            "Started development of Portfolio SaaS."
        ),
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
        value=4,
    ),
    Metric(
        name="Programming Languages",
        value=7,
    ),
    Metric(
        name="Databases",
        value=5,
    ),
    Metric(
        name="Current Roles",
        value=2,
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
            name="Python",
            category="Backend",
        ),
        Technology(
            name="Java",
            category="Backend",
        ),
        Technology(
            name="Go",
            category="Backend",
        ),
        Technology(
            name="TypeScript",
            category="Backend",
        ),
        Technology(
            name="FastAPI",
            category="Framework",
        ),
        Technology(
            name="Spring Boot",
            category="Framework",
        ),
        Technology(
            name="Angular",
            category="Framework",
        ),
        Technology(
            name="Kotlin",
            category="Mobile",
        ),
        Technology(
            name="Jetpack Compose",
            category="Mobile",
        ),
        Technology(
            name="PostgreSQL",
            category="Database",
        ),
        Technology(
            name="Neo4j",
            category="Database",
        ),
        Technology(
            name="Supabase",
            category="Database",
        ),
        Technology(
            name="Docker",
            category="DevOps",
        ),
        Technology(
            name="RabbitMQ",
            category="DevOps",
        ),
        Technology(
            name="Firebase",
            category="Cloud",
        ),
        Technology(
            name="Transformers",
            category="AI/ML",
        ),
        Technology(
            name="Celonis",
            category="Data",
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

    projects = {
        project.name: project
        for project in session.exec(
            select(Project)
        ).all()
    }

    technologies = {
        technology.name: technology
        for technology in session.exec(
            select(Technology)
        ).all()
    }

    relations = [
        # Intent Classification System
        ProjectTechnology(
            project_id=projects[
                "Intent Classification System"
            ].id,
            technology_id=technologies[
                "Python"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Intent Classification System"
            ].id,
            technology_id=technologies[
                "Docker"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Intent Classification System"
            ].id,
            technology_id=technologies[
                "RabbitMQ"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Intent Classification System"
            ].id,
            technology_id=technologies[
                "Transformers"
            ].id,
        ),

        # Series Recommendation System
        ProjectTechnology(
            project_id=projects[
                "Series Recommendation System"
            ].id,
            technology_id=technologies[
                "Java"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Series Recommendation System"
            ].id,
            technology_id=technologies[
                "Spring Boot"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Series Recommendation System"
            ].id,
            technology_id=technologies[
                "Neo4j"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Series Recommendation System"
            ].id,
            technology_id=technologies[
                "Angular"
            ].id,
        ),

        # WhereNow
        ProjectTechnology(
            project_id=projects[
                "WhereNow"
            ].id,
            technology_id=technologies[
                "Kotlin"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "WhereNow"
            ].id,
            technology_id=technologies[
                "Jetpack Compose"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "WhereNow"
            ].id,
            technology_id=technologies[
                "Firebase"
            ].id,
        ),

        # Portfolio SaaS
        ProjectTechnology(
            project_id=projects[
                "Portfolio SaaS"
            ].id,
            technology_id=technologies[
                "FastAPI"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Portfolio SaaS"
            ].id,
            technology_id=technologies[
                "PostgreSQL"
            ].id,
        ),
        ProjectTechnology(
            project_id=projects[
                "Portfolio SaaS"
            ].id,
            technology_id=technologies[
                "Docker"
            ].id,
        ),
    ]

    session.add_all(relations)
    session.commit()