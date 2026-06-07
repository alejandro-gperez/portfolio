"""
GitHub analytics schemas.
"""

from pydantic import BaseModel


class GitHubMetricResponse(BaseModel):
    """
    GitHub analytics metric.
    """

    metric_name: str
    metric_value: int