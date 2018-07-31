from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from .models import *

from django.core.validators import RegexValidator

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password',)


class UserProfileForm(forms.ModelForm):


    class Meta:
      model = UserProfile
      fields = ('first_name','last_name','address','email','dob','mobile_number',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('username','rating','comment','date',)


class EditProfileForm(forms.ModelForm):

    first_name  = forms.CharField(label='First Name')
    last_name   = forms.CharField(label='Last Name')
    address     = forms.CharField()
    email       = forms.EmailField()
    dob         = forms.DateField()
    mobile_number = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class Milk_rateForm(forms.ModelForm):
    class Meta:
        model = Daily_transactions
        fields = ('quantity','Fat','SNF',)
