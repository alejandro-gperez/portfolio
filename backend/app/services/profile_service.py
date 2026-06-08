"""
Profile service layer.

Contains business logic related to portfolio profile data.
"""

from sqlmodel import Session
from sqlmodel import select

from app.models.profile import Profile


class ProfileService:
    """
    Service responsible for profile operations.
    """

    @staticmethod
    def get_profile(session: Session) -> Profile | None:
        """
        Retrieve the portfolio profile.

        Args:
            session: Active database session.

        Returns:
            Profile | None: Profile entity if found.
        """
        statement = select(Profile)

        return session.exec(statement).first()