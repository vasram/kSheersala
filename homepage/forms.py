
from django.contrib.auth.models import User
from django import forms
from .models import *


class ContacForm(forms.ModelForm):


    class Meta:
      model = Contact
      fields = ('first_name','last_name','email','comment')





