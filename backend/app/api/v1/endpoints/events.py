"""
Event tracking API endpoints.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlmodel import Session

from app.core.database import get_session

from app.schemas.event import EventResponse

from app.services.event_service import EventService

router = APIRouter()


@router.get(
    "/",
    response_model=list[EventResponse],
)
def get_events(
    session: Session = Depends(get_session),
) -> list[EventResponse]:
    """
    Retrieve recent activity events.
    """

    events = EventService.get_recent_events(
        session
    )

    return [
        EventResponse(
            event_type=event.event_type,
            description=event.description,
            created_at=event.created_at,
        )
        for event in events
    ]