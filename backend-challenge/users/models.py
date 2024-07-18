from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Your custom fields and methods here
