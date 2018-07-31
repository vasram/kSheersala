
from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import  static

admin.site.site_header = "kSheersala"
urlpatterns = [
   # url(r'^accounts/', include('accounts.urls')),
    url(r'^seller/', include('seller.urls')),
    url(r'^staff/', include('staff.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls')),


] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)









