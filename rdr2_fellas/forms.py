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

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Both passwords don't match!"
            )

# Optional information for user profile
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('gaming_id', 'platform', 'gamerstyle', 'playstyle', 'message')
        help_texts = {
            'gaming_id': 'Share your PSN ID or Xbox Gamertag here.'
        }
