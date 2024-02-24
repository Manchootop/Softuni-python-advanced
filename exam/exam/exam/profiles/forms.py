from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from .models import Profile


class CreateProfileForm(forms.Form):
    class Meta:
        model = Profile
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = '__all__'




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
