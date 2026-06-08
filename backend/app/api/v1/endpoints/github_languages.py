"""
GitHub language endpoints.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlmodel import Session

from app.core.database import (
    get_session,
)

from app.schemas.github_language import (
    GitHubLanguageResponse,
)

from app.services.github_language_service import (
    GitHubLanguageService,
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[
        GitHubLanguageResponse
    ],
)
def get_languages(
    session: Session = Depends(
        get_session
    ),
) -> list[
    GitHubLanguageResponse
]:
    """
    Retrieve GitHub language statistics.
    """

    languages = (
        GitHubLanguageService.get_languages(
            session
        )
    )

    return [
        GitHubLanguageResponse(
            language=language.language,
            bytes_of_code=language.bytes_of_code,
        )
        for language in languages
    ]