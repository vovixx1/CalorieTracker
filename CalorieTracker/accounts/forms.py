# accounts/forms.py
from django import forms
from .models import UserProfile  # Correct import for UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']  # List the fields you want the user to be able to update
