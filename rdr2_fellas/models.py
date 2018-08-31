from django.db import models
from django.contrib.auth.models import User

# UserProfile model uses default User fields with 3 additional attributes
class UserProfile(models.Model):

    # Create relationship and add attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    platform = models.TextField(blank=True)
    message = models.TextField(blank=True)
    searching = models.BooleanField(blank=True)

    def __str__(self):
        return self.user.username