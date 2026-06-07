"""
Dashboard metric schemas.
"""

from pydantic import BaseModel


class MetricResponse(BaseModel):
    """
    Individual dashboard metric.
    """

    name: str
    value: int
    unit: str | None = None