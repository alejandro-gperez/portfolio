"""
GitHub metrics API endpoints.
"""

from fastapi import APIRouter

from app.schemas.github_metric import GitHubMetricResponse

router = APIRouter()


@router.get("/", response_model=list[GitHubMetricResponse])
def get_github_metrics() -> list[GitHubMetricResponse]:
    """
    Retrieve GitHub analytics.

    Returns:
        list[GitHubMetricResponse]: GitHub statistics.
    """
    return [
        GitHubMetricResponse(
            metric_name="Repositories",
            metric_value=12,
        ),
        GitHubMetricResponse(
            metric_name="Commits This Year",
            metric_value=542,
        ),
        GitHubMetricResponse(
            metric_name="Pull Requests",
            metric_value=36,
        ),
    ]