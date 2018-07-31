from .models import *
from django.conf.urls import url

from . import views

urlpatterns = [
          url(r'^home/$',                     views.seller_home,             name='home'),
          url(r'^profile/',                   views.seller_profile,         name='profile'),
          url(r'^transactions/',              views.daily_transactions,     name='transactions'),
          url(r'^milk_rate/$',                 views.milk_rate,              name='Milk_rate'),
          url(r'^review/',                    views.review,                 name ='review'),
          url(r'^register/$',                 views.register,              name='register'),
          url(r'^login/$',                    views.user_login,            name='login'),
   #       url(r'^index/$',                    views.index,                 name='index'),
          url(r'^try_login_again/$',          views.try_login_again,       name='try_login_again'),
          url(r'^restricted/$',               views.restricted,            name='restricted'),
          url(r'^logout/$',                   views.user_logout,           name='logout'),
          url(r'^profile_edit/$',             views.edit_profile, name='edit_profile'),
         # url(r'^profile_edit/$', views.edit_profile, name='edit_profile'),
        ]