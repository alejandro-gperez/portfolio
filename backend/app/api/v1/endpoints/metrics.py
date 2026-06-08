"""
Metrics API endpoints.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlmodel import Session

from app.core.database import get_session

from app.schemas.metric import (
    MetricResponse,
)

from app.services.metric_service import (
    MetricService,
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[MetricResponse],
)
def get_metrics(
    session: Session = Depends(get_session),
) -> list[MetricResponse]:
    """
    Retrieve dashboard metrics.

    Returns:
        list[MetricResponse]: Dashboard metrics.
    """

    metrics = MetricService.get_metrics(
        session
    )

    return [
        MetricResponse(
            name=metric.name,
            value=metric.value,
            unit=metric.unit,
        )
        for metric in metrics
    ]