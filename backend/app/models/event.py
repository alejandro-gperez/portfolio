"""
Event database model.

Represents activity events displayed throughout
the portfolio platform.
"""

from datetime import datetime
from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Event(SQLModel, table=True):
    """
    Portfolio activity event entity.
    """

    __tablename__ = "events"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    event_type: str

    description: str

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
    )