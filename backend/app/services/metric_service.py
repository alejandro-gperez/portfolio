"""
Metric service layer.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.metric import Metric


class MetricService:
    """
    Service responsible for dashboard metrics.
    """

    @staticmethod
    def get_metrics(
        session: Session,
    ) -> list[Metric]:
        """
        Retrieve dashboard metrics.
        """

        statement = select(Metric)

        return list(
            session.exec(statement).all()
        )