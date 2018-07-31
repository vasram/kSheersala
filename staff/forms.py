from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from .models import *
from seller.models import *

class StaffForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password',)



class StaffEditProfileForm(forms.ModelForm):

    first_name                = forms.CharField(label='First Name')
    last_name                 = forms.CharField(label='Last Name')
    address                   = forms.CharField()
    email                     = forms.EmailField()
    dob                       = forms.DateField()
    mobile_number             = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name']



class Daily_transactionsForm(forms.ModelForm):
    class Meta:
        model = Daily_transactions
        fields = ('username','transaction_date','quantity','Fat','SNF','cattle',)


class Get_seller_usernameForm(forms.ModelForm):
    class Meta:
        model = Sellers_Records
        fields =('username',)

class EditProfileForm2(forms.ModelForm):

    first_name  = forms.CharField(label='First Name')
    last_name   = forms.CharField(label='Last Name')
    address     = forms.CharField()
    email       = forms.EmailField()
    dob         = forms.DateField()
    class Meta:
        model = Sellers_Records
        fields = ['first_name', 'last_name']
