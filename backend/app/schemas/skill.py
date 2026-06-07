"""
Skill response schemas.
"""

from pydantic import BaseModel


class SkillResponse(BaseModel):
    """
    Technical skill representation.
    """

    name: str
    category: str
    level: int