from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    details = models.TextField()

    class Meta:
        db_table: str = "users"
