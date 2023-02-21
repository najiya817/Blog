from django import forms
from account.models import UserProfile

class ProfieForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']