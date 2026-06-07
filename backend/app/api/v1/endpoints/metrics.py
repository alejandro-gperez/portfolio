"""
Metrics API endpoints.
"""

from fastapi import APIRouter

from app.schemas.metric import MetricResponse

router = APIRouter()


@router.get("/", response_model=list[MetricResponse])
def get_metrics() -> list[MetricResponse]:
    """
    Retrieve engineering dashboard metrics.

    Returns:
        list[MetricResponse]: Dashboard metrics.
    """
    return [
        MetricResponse(
            name="Projects",
            value=1,
        ),
        MetricResponse(
            name="APIs",
            value=6,
        ),
        MetricResponse(
            name="Databases",
            value=1,
        ),
        MetricResponse(
            name="Years Coding",
            value=3,
        ),
    ]