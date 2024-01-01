from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    details = models.TextField()

    class Meta:
        db_table: str = "users"
