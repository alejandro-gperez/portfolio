"""
Projects API endpoints.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlmodel import Session

from app.core.database import get_session

from app.schemas.project import (
    FeatureResponse,
    ProjectResponse,
)

from app.services.project_service import (
    ProjectService,
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[ProjectResponse],
)
def get_projects(
    session: Session = Depends(get_session),
) -> list[ProjectResponse]:
    """
    Retrieve featured projects.
    """

    projects = (
        ProjectService.get_featured_projects(
            session
        )
    )

    return [
        ProjectResponse(
            id=project.id,
            name=project.name,
            description=project.description,
            status=project.status,
            featured=project.featured,
            github_url=project.github_url,
            demo_url=project.demo_url,
            stack=[],  # temporal
            features=[
                FeatureResponse(
                    name=feature.name
                )
                for feature in project.features
            ],
        )
        for project in projects
    ]