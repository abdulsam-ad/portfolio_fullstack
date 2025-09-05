from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    display_name = models.CharField(max_length=150, blank=True)
    def __str__(self) -> str:
        return self.username or self.email or str(self.pk)
