"""
Projects API endpoints.
"""

from fastapi import APIRouter

from app.schemas.project import (
    FeatureResponse,
    ProjectResponse,
)

router = APIRouter()


@router.get("/", response_model=list[ProjectResponse])
def get_projects() -> list[ProjectResponse]:
    """
    Retrieve featured portfolio projects.

    Returns:
        list[ProjectResponse]: Portfolio projects.
    """
    return [
        ProjectResponse(
            id=1,
            name="Portfolio SaaS",
            description="Personal backend-focused portfolio platform.",
            status="In Progress",
            featured=True,
            github_url="https://github.com/your-username/portfolio-saas",
            demo_url=None,
            stack=[
                "FastAPI",
                "PostgreSQL",
                "React",
            ],
            features=[
                FeatureResponse(
                    name="REST API",
                ),
                FeatureResponse(
                    name="GitHub Analytics",
                ),
                FeatureResponse(
                    name="Event Tracking",
                ),
                FeatureResponse(
                    name="Observability Dashboard",
                ),
            ],
        )
    ]