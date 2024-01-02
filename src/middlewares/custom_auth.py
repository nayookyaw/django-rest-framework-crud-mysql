
from typing import Any


class CustomAuth():
    def __init__(self, get_response) -> None:
        self.get_response: Any = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        print("Middleware processing request")

        response = self.get_response(request)

        # Code to be executed for each response before it's sent to the client.
        print("Middleware processing response")

        return response