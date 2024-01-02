from typing import Any
from django.utils import timezone

from datetime import timedelta

from knox.auth import TokenAuthentication
from knox.models import AuthToken, AuthTokenManager
from knox.settings import knox_settings

from ..user.models import User
from ..user.repositories import UserRepositories

class ExtendTokenExpirationMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response: Any = get_response

    def __call__(self, request):
        response = self.get_response(request)

        exist_user: User | None = UserRepositories.get_user_by_id(id=1)
        if exist_user is not None:
            user_tokens: AuthTokenManager = AuthToken.objects.filter(user=exist_user)

            # Delete each token
            for token in user_tokens:
                # Extend the expiration time by updating the token's expires field
                expiry: Any = knox_settings.TOKEN_TTL
                expiration_time: Any = timezone.now() + timedelta(hours=2)
                token.expiry = expiration_time
                token.save()

        return response
