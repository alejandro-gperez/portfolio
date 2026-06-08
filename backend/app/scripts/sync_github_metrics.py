"""
GitHub metrics synchronization script.

Fetches GitHub analytics data and updates
the portfolio database.
"""

from sqlmodel import Session
from sqlmodel import delete
from sqlmodel import select

from app.core.database import engine

from app.models.github_metric import (
    GitHubMetric,
)

from app.models.github_language import (
    GitHubLanguage,
)

from app.services.github_service import (
    GitHubService,
)


def sync_github_metrics() -> None:
    """
    Synchronize GitHub summary metrics.
    """

    summary_metrics = (
        GitHubService.get_summary_metrics()
    )

    with Session(engine) as session:
        session.exec(
            delete(GitHubMetric)
        )

        for (
            metric_name,
            metric_value,
        ) in summary_metrics.items():
            session.add(
                GitHubMetric(
                    metric_name=metric_name,
                    metric_value=metric_value,
                )
            )

        session.commit()

    print(
        "✓ GitHub metrics synchronized"
    )


def sync_github_languages() -> None:
    """
    Synchronize GitHub language statistics.
    """

    language_usage = (
        GitHubService.get_language_usage()
    )

    with Session(engine) as session:
        session.exec(
            delete(GitHubLanguage)
        )

        for (
            language,
            bytes_of_code,
        ) in language_usage.items():
            session.add(
                GitHubLanguage(
                    language=language,
                    bytes_of_code=bytes_of_code,
                )
            )

        session.commit()

    print(
        "✓ GitHub languages synchronized"
    )


def main() -> None:
    """
    Execute full GitHub synchronization.
    """

    print(
        "Starting GitHub synchronization..."
    )

    sync_github_metrics()

    sync_github_languages()

    print(
        "✓ Synchronization complete"
    )


if __name__ == "__main__":
    main()