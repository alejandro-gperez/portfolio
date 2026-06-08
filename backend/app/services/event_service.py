"""
Event service layer.

Contains business logic related to activity events.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.event import Event


class EventService:
    """
    Service responsible for event operations.
    """

    @staticmethod
    def get_recent_events(
        session: Session,
    ) -> list[Event]:
        """
        Retrieve recent activity events.

        Args:
            session: Active database session.

        Returns:
            list[Event]: Activity events.
        """
        statement = (
            select(Event)
            .order_by(Event.created_at.desc())
        )

        return list(
            session.exec(statement).all()
        )