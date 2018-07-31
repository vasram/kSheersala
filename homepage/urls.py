from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.home, name='index'),
    url(r'^contact/', views.contact, name='contact'),
   url(r'^about/', views.about, name='contact'),
]



