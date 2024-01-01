from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import authenticate

from knox.models import AuthToken

from typing import Any
from datetime import datetime

from ..utils.response_util import ResponseUtil
from .serializers import UserSerializer
from .request_body.user_add import UserAdd
from .repositories import UserRepositories

class UserServices():
    
    @classmethod
    def save_user(cls, request) -> Response:
        request_serializer: UserAdd = UserAdd (data=request.data)
        if request_serializer.is_valid():
            validated_data : Any = request_serializer.validated_data
            
            validated_data['password'] = make_password(password=validated_data.get("password"))

            # add for user base model
            validated_data['first_name'] = "system"
            validated_data['last_name'] = "system"
            validated_data['email'] = validated_data.get("email")
            validated_data['is_staff'] = False
            validated_data['is_active'] = True
            validated_data['date_joined'] = datetime.now()
            new_user : UserSerializer = UserSerializer(data=validated_data)

            UserRepositories.save_user(user_serializer=new_user)
            return ResponseUtil.custom_success_response(
                message="user has been saved successfully"
            )
        else:
            return ResponseUtil.custom_fail_response(
                message="validation failed"
            )
    
    @classmethod
    def login_user(cls, request) -> Response:
        username: str = "test"
        password: str = "1234"
        user: AbstractBaseUser | None = authenticate(username=username, password=password)
        if user is not None:
            knox_token: str = AuthToken.objects.create(user=user)[1]
            print (knox_token)
            return Response(data={"success": "success credentials"})
        else:
            return Response(data={"error": "Invalid credentials"})