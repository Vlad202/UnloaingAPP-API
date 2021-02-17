<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

class UserColor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usercolorcode')
    color = models.CharField(max_length=15)

    def __str__(self):
        return '{} - {}'.format(self.user.first_name, self.color)
=======
from django.db import models
from django.contrib.auth.models import User

class UserColor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usercolorcode')
    color = models.CharField(max_length=15)

    def __str__(self):
        return '{} - {}'.format(self.user.first_name, self.color)
>>>>>>> 28db349d9fc26775f91308aec53ddc052260599d
