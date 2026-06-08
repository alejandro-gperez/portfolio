"""
Dashboard metric database model.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Metric(SQLModel, table=True):
    """
    Dashboard metric entity.
    """

    __tablename__ = "metrics"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    name: str

    value: int

    unit: str | None = None