# custom_exception_handler.py

from typing import Any
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context) -> Response | None:
    # Call the default exception handler first
    response: Response | None = exception_handler(exc=exc, context=context)

    if response is not None:
        error_msg: str = str(exc)
        status_code: int = response.status_code

        return Response(data={"message" : error_msg, "status": status_code}, status=status_code)

    return response
