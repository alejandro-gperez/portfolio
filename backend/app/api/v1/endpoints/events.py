"""
Event tracking API endpoints.
"""

from datetime import datetime

from fastapi import APIRouter

from app.schemas.event import EventResponse

router = APIRouter()


@router.get("/", response_model=list[EventResponse])
def get_events() -> list[EventResponse]:
    """
    Retrieve recent activity events.

    Returns:
        list[EventResponse]: Recent activity.
    """
    return [
        EventResponse(
            event_type="PROJECT_CREATED",
            description="Portfolio SaaS project initialized.",
            created_at=datetime.now(),
        ),
        EventResponse(
            event_type="DEPLOYMENT",
            description="Initial API deployment completed.",
            created_at=datetime.now(),
        ),
    ]