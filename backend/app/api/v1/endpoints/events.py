"""
Event tracking API endpoints.

Provides recent portfolio activity and system events.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_events() -> list[dict]:
    """
    Retrieve recent activity events.

    Returns:
        list[dict]: Chronological activity log.
    """
    return [
        {
            "event_type": "PROJECT_CREATED",
            "description": "Portfolio SaaS project initialized.",
        },
        {
            "event_type": "DEPLOYMENT",
            "description": "Portfolio API deployed.",
        },
    ]