from __future__ import unicode_literals
from datetime import date
from datetime import  datetime
from django.core.validators import RegexValidator
from django.db import models


class  Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email      = models.EmailField(blank=True)
    comment    = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.first_name

