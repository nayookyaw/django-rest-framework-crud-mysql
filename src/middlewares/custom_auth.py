
from typing import Any
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from rest_framework.response import Response
from django.http import JsonResponse

from ..utils.response_util import ResponseUtil
class CustomAuth():
    def __init__(self, get_response) -> None:
        self.get_response: Any = get_response

    def __call__(self, request) -> Response | Any:
        # Code to be executed for each request before the view (and later middleware) are called.
        print("Middleware processing request")
        print (request.headers.get('Authorization'))

        response: Any = self.get_response(request)
        # if response.status_code == 200:
        #     response = JsonResponse(data={"message" : "unauthorized", "status" : HTTP_200_OK}, status=HTTP_200_OK)

        return response