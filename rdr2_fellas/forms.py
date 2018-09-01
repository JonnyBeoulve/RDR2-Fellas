from django import forms
from django.contrib.auth.models import User
from rdr2_fellas.models import UserProfile

class UserForm(forms.ModelForm):
    """ This class houses required information for user profile registration """

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

class UserProfileForm(forms.ModelForm):
    """ This class houses supplementary information for user profile registration """

    class Meta():
        model = UserProfile
        fields = ('gaming_id', 'platform', 'gamerstyle', 'playstyle', 'time_availability', 'day_availability')
        help_texts = {
            'gaming_id': 'Share your PSN ID or Xbox Gamertag here.'
        }

class UpdateUserProfileForm(forms.ModelForm):
    """ This class allows a user to update their information from the myprofile page """

    gaming_id = forms.CharField(required=True)
    platform = forms.CharField(required=True)
    gamerstyle = forms.CharField(required=True)
    playstyle = forms.CharField(required=True)
    time_availability = forms.CharField(required=True)
    day_availability = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ('gaming_id', 'platform', 'gamerstyle', 'playstyle', 'time_availability', 'day_availability')
        help_texts = {
            'gaming_id': 'Share your PSN ID or Xbox Gamertag here.'
        }

    def save(self, commit=True):
        user = super(UpdateUserProfileForm, self).clean()

        if commit:
            user.save()
        
        return user