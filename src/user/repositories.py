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
    
    @classmethod
    def get_user_by_id(cls, id: int) -> User | None:
        user: User | None = None
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            user = None
        
        return user