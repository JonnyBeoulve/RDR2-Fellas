from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    # Create relationship with default user model, but with added attributes
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    platform = models.TextField(blank=True)
    message = models.TextField(blank=True)
    searching = models.BooleanField(blank=True)

    def __str__(self):
        return self.user.username