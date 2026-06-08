"""
Skill database model.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Skill(SQLModel, table=True):
    """
    Technical skill entity.
    """

    __tablename__ = "skills"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    name: str

    category: str

    level: int