"""
Skills API endpoints.

Provides categorized technical skills.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlmodel import Session

from app.core.database import get_session
from app.schemas.skill import SkillResponse
from app.services.skill_service import SkillService

router = APIRouter()


@router.get("/", response_model=list[SkillResponse])
def get_skills(
    session: Session = Depends(get_session),
) -> list[SkillResponse]:
    """
    Retrieve all technical skills.

    Returns:
        list[SkillResponse]: Portfolio skills.
    """
    skills = SkillService.get_all_skills(
        session
    )

    return [
        SkillResponse(
            name=skill.name,
            category=skill.category,
            level=skill.level,
        )
        for skill in skills
    ]