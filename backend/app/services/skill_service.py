"""
Skill service layer.

Contains business logic related to portfolio skills.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.skill import Skill


class SkillService:
    """
    Service responsible for skill operations.
    """

    @staticmethod
    def get_all_skills(
        session: Session,
    ) -> list[Skill]:
        """
        Retrieve all portfolio skills.

        Args:
            session: Active database session.

        Returns:
            list[Skill]: Portfolio skills.
        """
        statement = select(Skill)

        return list(
            session.exec(statement).all()
        )