from rest_framework.exceptions import ValidationError

from .serializers import UserSerializer
from .models import User

class UserRepositories():
    
    @classmethod
    def save_user(cls, user_serializer: UserSerializer) -> User | None:
        if user_serializer.is_valid():
            return user_serializer.save()
        else:
            raise ValidationError(detail=user_serializer.errors)