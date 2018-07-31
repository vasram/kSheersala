# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import *


class Admin_UserProfile(admin.ModelAdmin):

    list_display         = ('username','first_name', 'last_name','email','mobile_number','dob','address',  )
    list_display_links   = ('first_name','first_name', 'last_name', )
   # ordering             = ('seller_id',)
    search_fields        = ('first_name','first_name', 'last_name',)


#admin.site.register(UserProfile)


admin.site.register(Sellers_Records,Admin_UserProfile)
admin.site.register(UserProfile)






class Admin_Daily_transaction(admin.ModelAdmin):

    list_display = ('username','transaction_date','cattle','Fat','SNF','quantity','payment',)
    list_display_links = ('username','transaction_date',)
    ordering           = ('username',)
    search_fields      = ('username',)


class Admin_Review(admin.ModelAdmin):
    list_display = ('username','comment','rating','date' )
    list_display_links = ('username',)
    ordering = ('username',)
    search_fields = ('username',)


admin.site.register(Daily_transactions,Admin_Daily_transaction)
admin.site.register(Review,Admin_Review)
