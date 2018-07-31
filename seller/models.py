
from __future__ import unicode_literals
from datetime import date
from datetime import  datetime
from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import User

now = datetime.now()
Cattle_choices = ( ('BUFFALO','Buffalo'),
                    ('COW' ,'Cow')
                 )


#from django.db import models
Gender_choice = ( ('MALE','Male'),
           ('FEMALE' ,'Female')
         )

marital_status = (('YES','yes'),
                  ('NO','no')
                  )

RATING_CHOICES = ( (1, 'One'),
                   (2, 'Two'),
                   (3, 'Three'),
                   (4, 'Four'),
                   (5, 'Five'))

class UserProfile(models.Model):
    user         = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=20)
    last_name   = models.CharField(max_length=20)
    address     = models.CharField(max_length=100, null=True)
    email        = models.EmailField(blank=True)
    dob          = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must have 10 digits.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=10, null=True)  # validators should be a list

    def __str__(self):
        return self.user.username


class Sellers_Records(models.Model):
    username   = models.CharField(max_length=20,primary_key=True )
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    address    = models.CharField(max_length=100, null=True)
    email      = models.EmailField(blank=True)
    dob        = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must have 10 digits.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=10, null=True)  # validators should be a list
    marital_status = models.CharField(max_length=20,choices=marital_status,default='YES')
    #mobile_number = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.username








class Daily_transactions(models.Model):
    username         =   models.CharField(max_length=20, null=True)
    transaction_date =   models.DateTimeField(default=now)
    quantity         =   models.FloatField()
    Fat              =   models.FloatField(max_length=10,null=True)
    SNF              =   models.FloatField(max_length=10, null=True)
    cattle           =   models.CharField(max_length=10, choices=Cattle_choices, default='BUFFALO')
    payment          =   models.FloatField(null=True)
    transaction_id   =   models.AutoField(primary_key=True)
    def __unicode__(self):
        return str(self.username)


class Review(models.Model):

    rating         = models.IntegerField ('Rating (stars)', blank=False, choices=RATING_CHOICES)
    comment        = models.CharField(max_length=10000 ,blank=True, null=True)
    username       = models.CharField(max_length=20,null=True)
    date           = models.DateTimeField(default=now)


    def __unicode__(self):
        return str(self.username )


