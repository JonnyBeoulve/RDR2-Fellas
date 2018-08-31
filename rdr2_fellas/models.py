from django.db import models
from django.contrib.auth.models import User

# UserProfile model uses default User fields with 3 additional attributes
class UserProfile(models.Model):

    # Create relationship and add attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    searching = models.BooleanField(blank=True)
    platform = models.CharField(max_length=14,blank=False)
    gaming_id = models.CharField(max_length=20,blank=False)
    message = models.TextField(max_length=255,blank=False)

    def __str__(self):
        return self.user.username