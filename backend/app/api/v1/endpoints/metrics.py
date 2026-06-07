"""
Metrics API endpoints.

Provides dashboard metrics used in the Engineering
Overview section.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_metrics() -> dict:
    """
    Retrieve portfolio summary metrics.

    Returns:
        dict: High-level engineering metrics.
    """
    return {
        "projects": 1,
        "apis": 1,
        "databases": 1,
        "years_coding": 3,
    }