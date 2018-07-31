
from __future__ import unicode_literals
from datetime import date
from datetime import  datetime
now = datetime.now()
from django.db import models
from seller.models import *
from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField




gender = ( ('MALE','Male'),
           ('FEMALE' ,'Female')
         )

Cattle_choices = ( ('BUFFALO','buffalo'),
                    ('COW' ,'cow')
                 )


class StaffProfile(models.Model):
    user = models.OneToOneField(User)




class Staff_Record(models.Model):
    first_name       =   models.CharField(max_length=100)
    last_name        =   models.CharField(max_length=100)
    username         =   models.CharField(max_length=100, primary_key=True)
    email            =   models.EmailField(null=True)
   # mobile_number    =   PhoneNumberField(null=True)
    gender           =   models.CharField(max_length=100,choices=gender,default='MALE')
    dob               = models.DateField(null=True)
    address          =   models.CharField(max_length=100)
    join_date        =   models.DateField(default=date.today)
    salary           =   models.IntegerField()
    work             =   models.CharField(max_length=100,null=True)
   # staff_image      =   models.ImageField(upload_to="staff/static/staff_img", blank=True, null=True)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must have 10 digits.")
    mobile_number   = models.CharField(validators=[phone_regex], max_length=10, null=True)  # validators should be a lis
    def __unicode__(self):
        return self.first_name + " "+ self.last_name

class Bill_detail(models.Model):

     seller_id      = models.ForeignKey(Sellers_Records,on_delete=models.CASCADE)
     payment        = models.IntegerField()
     bill_id        = models.IntegerField()
     submit_date    = models.DateTimeField(default=now)

     def __unicode__(self):
        return str(self.bill_id)

class Milk_rate(models.Model):
    Kg_Fat_Rate   = models.FloatField(max_length=10)
    Kg_SNF_Rate    = models.FloatField(max_length=10)
    #cattle        = models.CharField(max_length=10, choices=Cattle_choices, default='COW')
    up_date       = models.DateTimeField(default=now)

    def __unicode__(self):
        return str(self.Kg_Fat_Rate)