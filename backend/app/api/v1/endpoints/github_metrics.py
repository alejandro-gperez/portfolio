"""
GitHub metrics API endpoints.

Provides analytics generated from GitHub activity
and data pipeline processing.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_github_metrics() -> dict:
    """
    Retrieve GitHub activity metrics.

    Returns:
        dict: Aggregated GitHub statistics.
    """
    return {
        "repositories": 12,
        "commits_this_year": 542,
        "pull_requests": 36,
        "stars_received": 18,
    }