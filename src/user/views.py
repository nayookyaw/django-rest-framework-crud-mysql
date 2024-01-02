from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


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
    authentication_classes: Any = []
    permission_classes: Any = [AllowAny,]

    def post(self, request) -> Response:
        try:
            return UserServices.login_user(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))

class UserLogout(APIView):
    authentication_classes: Any = []
    permission_classes: Any = [AllowAny,]

    def post(self, request) -> Response:
        try:
            return UserServices.logout_user(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))