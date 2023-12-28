from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

class ResponseUtil:
    @classmethod
    def custom_success_response (cls, message: str, data = None, status: int = HTTP_200_OK) -> Response:
        return Response(data={"data" : data, "message" : message, "status" : status}, status=HTTP_200_OK)

    @classmethod
    def custom_fail_response (cls, message: str, status: int= HTTP_400_BAD_REQUEST) -> Response:
        return Response(data={"message" : message, "status" : status}, status=HTTP_200_OK)

    @classmethod
    def custom_error_response (cls, message: str, status: int= HTTP_500_INTERNAL_SERVER_ERROR) -> Response:
        return Response(data={"message" : message, "status": status}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def custom_unauthorized_response (cls, message: str, status: int= HTTP_401_UNAUTHORIZED) -> Response:
        return Response(data={"message" : message, "status": status}, status=HTTP_401_UNAUTHORIZED)