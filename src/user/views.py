from rest_framework.views import APIView
from knox.models import AuthToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractBaseUser

from ..utils.response_util import ResponseUtil
from .services import UserServices

class UserView(APIView):
    def post(self, request, pk:int) -> Response:
        try:
            return UserServices.save_user(request=request)
        except Exception as error:
            return ResponseUtil.custom_error_response(message=str(error))

class UserList(APIView):
    pass

class UserLogin(APIView):
    def post(self, request, pk:int) -> Response:
        username: str = "test"
        password: str = "1234"
        user: AbstractBaseUser | None = authenticate(username=username, password=password)
        if user is not None:
            knox_token: str = AuthToken.objects.create(user=user)[1]
            print (knox_token)
            return Response(data={"success": "success credentials"})
        else:
            return Response(data={"error": "Invalid credentials"})
