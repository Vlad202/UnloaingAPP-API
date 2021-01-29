from django.db import models
from django.contrib.auth.models import User

class UserColor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usercolorcode')
    color = models.CharField(max_length=15)
