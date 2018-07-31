
from __future__ import unicode_literals

from django.contrib import admin


from .models import *


class Admin_Contact(admin.ModelAdmin):

    list_display         = ('first_name', 'last_name',  )
    list_display_links   = ('first_name', 'last_name', )
   # ordering             = ('seller_id',)
    search_fields        = ('first_name', 'last_name','email')


#admin.site.register(UserProfile)


admin.site.register(Contact,Admin_Contact)