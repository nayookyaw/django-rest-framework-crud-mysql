from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    details = models.TextField()

    class Meta:
        db_table: str = "users"
