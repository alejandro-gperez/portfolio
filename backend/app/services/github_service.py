"""
GitHub metric service layer.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.github_metric import (
    GitHubMetric,
)


class GitHubMetricService:
    """
    Service responsible for GitHub analytics.
    """

    @staticmethod
    def get_metrics(
        session: Session,
    ) -> list[GitHubMetric]:
        """
        Retrieve GitHub metrics.
        """

        statement = select(
            GitHubMetric
        )

        return list(
            session.exec(statement).all()
        )