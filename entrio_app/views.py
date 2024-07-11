import json

import requests
from django.http import JsonResponse

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from entrio_app.util import get_github_api_url, get_github_api_headers, create_repository_row


@require_http_methods(["GET"])
def get_repository_details(request, repository_first_name, repository_last_name):
    try:
        github_api_url = get_github_api_url(
            repository_first_name=repository_first_name,
            repository_last_name=repository_last_name,
        )

        github_api_headers = get_github_api_headers()

        result = requests.get(
            url=github_api_url,
            headers=github_api_headers,
        )

        if result.status_code == 404:
            response_data = {
                "response": {
                    "success": False,
                    "created": False,
                    "error": "repository wasn't found",
                }
            }

            response = JsonResponse(
                data=response_data,
                status=404,
            )

            return response

        json_result = result.json()

        created, repository = create_repository_row(
            json_result=json_result,
        )

        response_data = {
            "response": {
                "success": True,
                "created": created,
                "repository": repository,
            }
        }

        response = JsonResponse(
            data=response_data,
            status=200
        )

        return response

    except Exception as e:
        response_data = {
            "response": {
                "success": False,
                "created": False,
                "error": str(e),
            }
        }

        response = JsonResponse(
            data=response_data,
            status=500,
        )

        return response
