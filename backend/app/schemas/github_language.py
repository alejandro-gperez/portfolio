"""
GitHub language response schemas.
"""

from pydantic import BaseModel


class GitHubLanguageResponse(
    BaseModel
):
    """
    GitHub language usage representation.
    """

    language: str

    bytes_of_code: int