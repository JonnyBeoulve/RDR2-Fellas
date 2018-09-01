from django.db import models
from django.contrib.auth.models import User

# Tuples for fields with predefined choices
PLATFORM_CHOICES = (
    ('PlayStation 4', 'PlayStation 4'),
    ('Xbox One', 'Xbox One'),
)

GAMERSTYLE_CHOICES = (
    ('Casual', 'Casual'),
    ('Moderate', 'Moderate'),
    ('Hardcore', 'Hardcore'),
)

PLAYSTYLE_CHOICES = (
    ('Adventurer', 'Adventurer'),
    ('Competitor', 'Competititor'),
    ('Hunter', 'Hunter'),
    ('Level Grinder', 'Level Grinder'),
    ('Money Maker', 'Money Maker'),
    ('Royale Fiend', 'Royale Fiend'),
)

TIME_AVAILABILITY_CHOICES = (
    ('Any Time', 'Any Time'),
    ('Morning', 'Morning'),
    ('Noon', 'Noon'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
)

DAY_AVAILABILITY_CHOICES = (
    ('Every Day', 'Every Day'),
    ('Weekdays', 'Weekdays'),
    ('Weekends', 'Weekends'),
)

# UserProfile model references User field and contains several customizable attributes
class UserProfile(models.Model):

    # Create relationship and add attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gaming_id = models.CharField(max_length=16, blank=False)
    platform = models.CharField(max_length=13, choices=PLATFORM_CHOICES, default='PlayStation 4', blank=False)
    gamerstyle = models.CharField(max_length=13, choices=GAMERSTYLE_CHOICES, default='Casual', blank=False)
    playstyle = models.CharField(max_length=13, choices=PLAYSTYLE_CHOICES, default='Adventurer', blank=False)
    time_availability = models.CharField(max_length=13, choices=TIME_AVAILABILITY_CHOICES, default='Any Time', blank=False)
    day_availability = models.CharField(max_length=13, choices=DAY_AVAILABILITY_CHOICES, default='Every Day', blank=False)

    def __str__(self):
        return self.user.username