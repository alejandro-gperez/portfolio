"""
GitHub language analytics model.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class GitHubLanguage(
    SQLModel,
    table=True,
):
    """
    GitHub language usage statistics.
    """

    __tablename__ = (
        "github_languages"
    )

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    language: str

    bytes_of_code: int