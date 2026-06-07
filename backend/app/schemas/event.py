"""
Event tracking schemas.
"""

from datetime import datetime

from pydantic import BaseModel


class EventResponse(BaseModel):
    """
    Activity event representation.
    """

    event_type: str
    description: str
    created_at: datetime