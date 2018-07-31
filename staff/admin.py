from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class Admin_Staff_Record(admin.ModelAdmin):
    list_display         = ('first_name', 'last_name', 'username','email','gender','dob','mobile_number', )
    list_display_links   = ('first_name', 'username',)
    ordering             = ('username',)
    search_fields        = ('first_name',)

"""class Admin_Bill_detail(admin.ModelAdmin):
    list_display         = ('bill_id', 'seller_id', 'submit_date', )
    list_display_links   = ('bill_id','seller_id',)
    ordering             = ('bill_id',)
    search_fields        = ('bill_id',)
"""
class Admin_Milk_rate(admin.ModelAdmin):
    list_display = ('Kg_Fat_Rate','Kg_SNF_Rate','up_date',)
    list_display_links = ('Kg_Fat_Rate','Kg_SNF_Rate',)


admin.site.register(Staff_Record,Admin_Staff_Record)
#admin.site.register(Bill_detail ,Admin_Bill_detail)
admin.site.register(Milk_rate ,Admin_Milk_rate)