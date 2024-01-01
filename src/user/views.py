from rest_framework.views import APIView
from rest_framework.response import Response

from ..utils.response_util import ResponseUtil
from .services import UserServices

class UserView(APIView):
    def post(self, request, pk:int=0) -> Response:
        try:
            return UserServices.save_user(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))

class UserList(APIView):
    pass

class UserLogin(APIView):
    def post(self, request) -> Response:
        try:
            return UserServices.login_user(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))
