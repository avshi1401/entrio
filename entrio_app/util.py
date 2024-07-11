import json
from urllib.parse import urljoin

from django.forms import model_to_dict

from entrio.settings import GITHUB_API_PATH, GITHUB_API_TOKEN
from entrio_app.models import Repositories


def get_github_api_url(repository_first_name, repository_last_name):
    """
    This function is used before making a 'github' API call, in order to get the full url path for the specific
    repository.
    """
    github_api_url = urljoin(GITHUB_API_PATH, f'{repository_first_name}/{repository_last_name}')

    return github_api_url


def get_github_api_headers():
    """
    This function is used before making a 'github' API call, in order to get the headers for the request.
    """
    github_api_headers = {
        'Authorization': GITHUB_API_TOKEN,
    }

    return github_api_headers


def create_repository_row(json_result):
    """
    This function is used after the 'github' API has returned valid repository data.
    """
    if isinstance(json_result, list):
        json_result = json_result[0]

    created = False

    repository = Repositories.objects.filter(
        id=json_result['id'],
    ).first()

    if repository:
        repository_dict = model_to_dict(
            instance=repository,
        )

        return created, repository_dict

    repository = Repositories(
        name=json_result['full_name'],
        id=json_result['id'],
        stars=json_result['stargazers_count'],
        owner=json_result['owner']['login'],
        description=json_result['description'],
        forks=json_result['forks'],
        languages=json_result['language'],
        number_of_forks=json_result['forks_count'],
        topics=json_result['topics']
    )

    repository.save()
    created = True

    repository_dict = model_to_dict(
        instance=repository
    )

    return created, repository_dict
