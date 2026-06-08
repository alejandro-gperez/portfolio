"""
GitHub metric database model.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class GitHubMetric(SQLModel, table=True):
    """
    GitHub analytics metric entity.
    """

    __tablename__ = "github_metrics"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    metric_name: str

    metric_value: int