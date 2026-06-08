"""
GitHub language service layer.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.github_language import (
    GitHubLanguage,
)


class GitHubLanguageService:
    """
    Service responsible for GitHub language operations.
    """

    @staticmethod
    def get_languages(
        session: Session,
    ) -> list[GitHubLanguage]:
        """
        Retrieve GitHub language statistics.

        Args:
            session: Active database session.

        Returns:
            list[GitHubLanguage]:
                Language statistics.
        """

        statement = select(
            GitHubLanguage
        )

        return list(
            session.exec(statement).all()
        )