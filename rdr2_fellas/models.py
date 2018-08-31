from django.db import models
from django.contrib.auth.models import User

# Tuples for fields with predefined choices
PLATFORM_CHOICES = (
    ('ps4', 'PlayStation 4'),
    ('xbo', 'Xbox One'),
)

GAMERSTYLE_CHOICES = (
    ('casual', 'Competititor'),
    ('moderate', 'Moderate'),
    ('hardcore', 'Hardcore'),
)

PLAYSTYLE_CHOICES = (
    ('adventurer', 'Adventurer'),
    ('competitor', 'Competititor'),
    ('hunter', 'Hunter'),
    ('level_grinder', 'Level Grinder'),
    ('money_maker', 'Money Maker'),
    ('royale_fiend', 'Royale Fiend'),
)

# UserProfile model uses default User fields with 3 additional attributes
class UserProfile(models.Model):

    # Create relationship and add attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gaming_id = models.CharField(max_length=16,blank=False)
    platform = models.CharField(max_length=13, choices=PLATFORM_CHOICES, default='ps4', blank=False)
    gamerstyle = models.CharField(max_length=13, choices=GAMERSTYLE_CHOICES, default='casual', blank=False)
    playstyle = models.CharField(max_length=13, choices=PLAYSTYLE_CHOICES, default='adventurer', blank=False)
    message = models.TextField(max_length=128,blank=False)

    def __str__(self):
        return self.user.username