"""
Project service layer.

Contains business logic related to portfolio projects.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.project import Project


class ProjectService:
    """
    Service responsible for project operations.
    """

    @staticmethod
    def get_all_projects(
        session: Session,
    ) -> list[Project]:
        """
        Retrieve all portfolio projects.

        Args:
            session: Active database session.

        Returns:
            list[Project]: Portfolio projects.
        """
        statement = select(Project)

        return list(
            session.exec(statement).all()
        )

    @staticmethod
    def get_featured_projects(
        session: Session,
    ) -> list[Project]:
        """
        Retrieve featured projects.

        Args:
            session: Active database session.

        Returns:
            list[Project]: Featured projects.
        """
        statement = select(Project).where(
            Project.featured.is_(True)
        )

        return list(
            session.exec(statement).all()
        )