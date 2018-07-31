from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import*
# Create your views here.
#from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *

def home(request):

    return render(request,'homepage/base.html')

#def contact(request):
   # return render(request, 'homepage/contact.html',{'content':['If you would like to contact me, please email me.','vasramparmar@gmail.com']})

def contact(request):
    if request.method == 'POST':
        review_form = ContacForm(data=request.POST)

        if review_form.is_valid():
            review_form.save()

            return HttpResponseRedirect('/home/')
        else:

            return render(request, 'homepage/contact.html',{'ContacForm': ContacForm, }, )
    else:
        review_form = ContacForm()
        return render(request, 'homepage/contact.html', {'ContacForm': ContacForm, }, )


def about(request):
    return  render(request,'homepage/about_us.html')