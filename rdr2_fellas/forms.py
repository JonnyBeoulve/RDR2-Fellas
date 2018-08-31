from django import forms
from django.contrib.auth.models import User
from rdr2_fellas.models import UserProfile

# Required information for user profile registration
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

# Optional information for user profile
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('platform', 'message', 'searching')
