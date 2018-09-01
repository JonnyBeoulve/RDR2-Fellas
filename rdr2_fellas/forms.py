from django import forms
from django.contrib.auth.models import User
from rdr2_fellas.models import UserProfile

# Required information for user profile registration
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    # Check that passwords match and are at least 6 chars in length
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Both passwords don't match!"
            )
        elif len(password) < 6:
            raise forms.ValidationError(
                'Password must be at least 6 characters in length!'
                )

# Optional information for user profile
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('gaming_id', 'platform', 'gamerstyle', 'playstyle', 'time_availability', 'day_availability')
        help_texts = {
            'gaming_id': 'Share your PSN ID or Xbox Gamertag here.'
        }
