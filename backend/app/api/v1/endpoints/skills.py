"""
Skills API endpoints.

Provides categorized technical skills.
"""

from fastapi import APIRouter

from app.schemas.skill import SkillResponse

router = APIRouter()


@router.get("/", response_model=list[SkillResponse])
def get_skills() -> list[SkillResponse]:
    """
    Retrieve technical skills.

    Returns:
        list[SkillResponse]: Portfolio skills.
    """
    return [
        SkillResponse(
            name="FastAPI",
            category="Backend",
            level=5,
        ),
        SkillResponse(
            name="PostgreSQL",
            category="Database",
            level=4,
        ),
        SkillResponse(
            name="Docker",
            category="DevOps",
            level=4,
        ),
        SkillResponse(
            name="Pandas",
            category="Data",
            level=4,
        ),
    ]