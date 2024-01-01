
from .serializers import UserSerializer
from .models import User

class UserRepositories():
    
    @classmethod
    def save_user(cls, user_serializer: UserSerializer) -> User | None:
        if user_serializer.is_valid():
            print ("going to save")
            return user_serializer.save()
        print (user_serializer.errors)
        return None