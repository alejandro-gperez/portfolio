"""
GitHub service layer.

Responsible for communicating with the GitHub REST API
and transforming external data into application-friendly
structures.
"""

from collections import defaultdict

import requests

from app.core.config import settings


class GitHubService:
    """
    Service responsible for GitHub API interactions.
    """

    BASE_URL = "https://api.github.com"

    @staticmethod
    def _headers() -> dict[str, str]:
        """
        Build GitHub API request headers.

        Returns:
            dict[str, str]: Authenticated request headers.
        """

        return {
            "Authorization": (
                f"Bearer {settings.GITHUB_TOKEN}"
            ),
            "Accept": (
                "application/vnd.github+json"
            ),
        }

    @classmethod
    def get_user_profile(
        cls,
    ) -> dict:
        """
        Retrieve GitHub user profile.

        Returns:
            dict: GitHub user data.
        """

        response = requests.get(
            f"{cls.BASE_URL}/users/"
            f"{settings.GITHUB_USERNAME}",
            headers=cls._headers(),
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    @classmethod
    def get_repositories(
        cls,
    ) -> list[dict]:
        """
        Retrieve public repositories.

        Returns:
            list[dict]: Repository metadata.
        """

        response = requests.get(
            f"{cls.BASE_URL}/users/"
            f"{settings.GITHUB_USERNAME}/repos",
            headers=cls._headers(),
            params={
                "per_page": 100,
                "sort": "updated",
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    @classmethod
    def get_summary_metrics(
        cls,
    ) -> dict[str, int]:
        """
        Build summary GitHub metrics.

        Returns:
            dict[str, int]: Dashboard metrics.
        """

        profile = cls.get_user_profile()

        repositories = (
            cls.get_repositories()
        )

        total_stars = sum(
            repo["stargazers_count"]
            for repo in repositories
        )

        total_forks = sum(
            repo["forks_count"]
            for repo in repositories
        )

        return {
            "Repositories": len(
                repositories
            ),
            "Followers": profile[
                "followers"
            ],
            "Following": profile[
                "following"
            ],
            "Stars": total_stars,
            "Forks": total_forks,
        }

    @classmethod
    def get_language_usage(
        cls,
    ) -> dict[str, int]:
        """
        Aggregate language statistics across all repositories.

        Returns:
            dict[str, int]:
                Language -> bytes of code.
        """

        repositories = (
            cls.get_repositories()
        )

        language_totals = defaultdict(
            int
        )

        for repo in repositories:
            language_url = repo[
                "languages_url"
            ]

            response = requests.get(
                language_url,
                headers=cls._headers(),
                timeout=10,
            )

            response.raise_for_status()

            languages = (
                response.json()
            )

            for (
                language,
                bytes_of_code,
            ) in languages.items():
                language_totals[
                    language
                ] += bytes_of_code

        return dict(
            language_totals
        )