from django.conf.urls import url

from . import views
import json
urlpatterns = [
    url(r'^$',                  views.index,                       name='index'),
    url(r'^home/$',             views.staff_home,                  name='home'),
    url(r'^register/$',         views.register,                    name='register'),
    url(r'^login/$',            views.staff_login,                 name='login'),
    url(r'^try_login_again/$',  views.try_login_again,             name='try_login_again'),
    url(r'^logout/$',           views.user_logout,                 name='logout'),
    url(r'^profile/$',          views.staff_profile,               name='staff_profile'),
    url(r'^profile_edit/$',     views.edit_profile,                name='edit_profile'),
    url(r'^dailytransactions/$',views.dailyTransactions,           name='DailyTransactions'),
    url(r'^getseller/$',        views.getseller,                   name='getseller'),
    url(r'^review/$',           views.review,                      name='review'),
    url(r'^alltransactionshistory/$',views.alltransactionshistory, name='alltransactionshistory'),
    url(r'^delete_seller_record/$', views.delete_seller_record,    name='delete_seller_record'),
    url(r'^update_seller_record/$', views.update_seller_record,    name='update_seller_record'),
    url(r'^payment/$',              views.payment,                 name='payment'),
    url(r'^milk_price/$',            views.milk_price,                 name='milk_price'),
]



