"""
GitHub metrics API endpoints.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlmodel import Session

from app.core.database import (
    get_session,
)

from app.schemas.github_metric import (
    GitHubMetricResponse,
)

from app.services.github_metric_service import (
    GitHubMetricService,
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[
        GitHubMetricResponse
    ],
)
def get_github_metrics(
    session: Session = Depends(
        get_session
    ),
) -> list[
    GitHubMetricResponse
]:
    """
    Retrieve GitHub analytics.
    """

    metrics = (
        GitHubMetricService.get_metrics(
            session
        )
    )

    return [
        GitHubMetricResponse(
            metric_name=metric.metric_name,
            metric_value=metric.metric_value,
        )
        for metric in metrics
    ]