# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
from django.http import HttpResponse
from .models import *
from staff.models import*

from .forms import UserForm, UserProfileForm, ReviewForm ,EditProfileForm,Milk_rateForm
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

#seller register
def register(request):
    # if any user already login
    if request.user.is_authenticated():
        username = request.user.username
        # user_record = Staff_Record.objects.get(username=username)
        if len(Sellers_Records.objects.filter(username=username)) != 0:
            return HttpResponseRedirect('/seller/home/')
        elif len(Staff_Record.objects.filter(username=username)) != 0:
            return HttpResponseRedirect('/staff/home/')
    context = RequestContext(request)
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)


        # check if already registered
        username = user_form['username'].value()
        if len(User.objects.filter(username=username)) != 0:
            message = 'An account already exists with this username !'
            return render(request,
                          'seller/register.html',
                          {'user_form': user_form,
                           'profile_form': profile_form,
                           'message': message, })



        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True


            # fill the seller table
            seller_username    = user_form['username'].value()
            seller_first_name = profile_form['first_name'].value()
            seller_last_name = profile_form['last_name'].value()
            seller_address = profile_form['address'].value()
            seller_email   = profile_form['email'].value()
            seller_dob= profile_form['dob'].value()
            seller_mobile_number = profile_form['mobile_number'].value()
            record = Sellers_Records(username=seller_username,
                                     first_name=seller_first_name,
                                     last_name=seller_last_name,
                                     address=seller_address,
                                     email=seller_email,
                                     dob=seller_dob,
                                     mobile_number = seller_mobile_number
                                     )
            record.save()


            return HttpResponseRedirect('/seller/login/')
        else:
            return render(request,
                          'seller/register.html',
                          {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
    else:
            user_form = UserForm()
            profile_form = UserProfileForm()

            return render(request,
                'seller/register.html',
                {'user_form': user_form, 'profile_form': profile_form, 'registered':registered})



#seller login
def user_login(request):
    # if any user already login
    if  request.user.is_authenticated():
        username = request.user.username
        #user_record = Staff_Record.objects.get(username=username)
        if len(Sellers_Records.objects.filter(username=username)) != 0:
           return HttpResponseRedirect('/seller/home/')
        else:
            return HttpResponseRedirect('/staff/home/')
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and len(Sellers_Records.objects.filter(username=username)) != 0:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/seller/home/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            #print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponseRedirect('/seller/try_login_again/')
    else:
        return render(request,'seller/login.html', {})

def try_login_again(request):
        return HttpResponse("<p>  User not exits , try again , Please give correct user name and password  .. "
                            "</br>"
                            "<a href='/seller/login/'>LOGIN</a>"
                            "</p>")


#seller logout
@login_required(login_url='/seller/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')



#seller home page
@login_required (login_url='/seller/login/')
def seller_home(request):
    username = request.user.username
    if len(Sellers_Records.objects.filter(username=username)) != 0:
        user_record = Sellers_Records.objects.get(username=username)
        return render(request,'seller/base.html',{'user_record': user_record },)
    else:
        return HttpResponseRedirect('/staff/home/')


#seller profile page
@login_required (login_url='/seller/login/')
def seller_profile(request):
    username = request.user.username
    user_record = Sellers_Records.objects.get(username=username)
    return render(request,'seller/profile.html',{'user_record': user_record},)


#seller daily transactions
@login_required (login_url='/seller/login/')
def daily_transactions(request):
    username = request.user.username
    user_record = Sellers_Records.objects.get(username=username)
    username = request.user.username
    transactions_record = Daily_transactions.objects.filter(username=username).order_by("-transaction_date")[:12]

    return render(request, 'seller/transactions.html', {'transactions_record': transactions_record ,'user_record': user_record}, )



def calculate_price(quantity, Fat, SNF):
    UpdatePrice =  Milk_rate.objects.order_by("-up_date")[:1]
    for first in UpdatePrice:
       x = first.Kg_Fat_Rate
       y = first.Kg_SNF_Rate
    payment = float(quantity) * ((float(x) * float(Fat)) + (float(y) * float(SNF)))
    return payment

#seller daily transactions
@login_required (login_url='/seller/login/')
def milk_rate(request):
    username    = request.user.username
    user_record = Sellers_Records.objects.get(username=username)

    context = RequestContext(request)
    if request.method == 'POST':
        transactions_form = Milk_rateForm(data=request.POST)
      #  username1 = transactions_form['username'].value()
        quantity = request.POST['quantity']
        Fat = request.POST['Fat']
        SNF = request.POST['SNF']

        payment = calculate_price(quantity, Fat, SNF)

        if transactions_form.is_valid():


            return render(request, 'seller/milk_rate.html', {'transactions_form':transactions_form,'payment': payment, 'user_record': user_record}, )
        else:
            return render(request, 'seller/milk_rate.html', {'transactions_form':transactions_form,'user_record': user_record}, )

    else:
        transactions_form = Milk_rateForm()
        return render(request, 'seller/milk_rate.html', { 'transactions_form':transactions_form,'user_record': user_record}, )




@login_required (login_url='/seller/login/')
def review(request):
    username    = request.user.username
    user_record = Sellers_Records.objects.get(username=username)
    context     = RequestContext(request)
    if request.method == 'POST':
      review_form = ReviewForm(data=request.POST)
      username1   = review_form['username'].value()
      username    = request.user.username
      if review_form.is_valid() and (username==username1):
         review_form.save()

         return HttpResponseRedirect('/seller/home/')
      else:
          message = 'Username invalid'
          return render(request,'seller/review.html',{'review_form': review_form,'user_record': user_record,'message':message},)
    else:
        review_form = ReviewForm()
        return render(request, 'seller/review.html', {'review_form': review_form,'user_record': user_record}, )


@login_required (login_url='/seller/login/')
def edit_profile(request):
    username = request.user.username
    user_record = Sellers_Records.objects.get(username=username)
    context = RequestContext(request)
    username = request.user.username
    user_record = Sellers_Records.objects.get(username=username)
    form = EditProfileForm(request.POST or None, initial={'first_name':user_record.first_name, 'last_name':user_record.last_name , 'address':user_record.address,'email':user_record.email,'dob':user_record.dob,'mobile_number':user_record.mobile_number})
    if request.method == 'POST':
        if form.is_valid():
            #For Seller_Record Update
            user_record.first_name            = request.POST['first_name']
            user_record.last_name             = request.POST['last_name']
            user_record.address               = request.POST['address']
            user_record.email                 = request.POST['email']
            user_record.dob                   = request.POST['dob']
            user_record.mobile_number         = request.POST['mobile_number']
            user_record.save()

            #Users Update

            User_record                      = User.objects.get(username=username)
            User_record.first_name           = user_record.first_name
            User_record.last_name            = user_record.last_name
            User_record.save()

            # seller UserProfile Update
            UserProfile_record               = UserProfile.objects.get(user__username=request.user.username)
            UserProfile_record.address       = user_record.address
            UserProfile_record.first_name    = user_record.first_name
            UserProfile_record.last_name     = user_record.last_name
            UserProfile_record.address       =user_record.address
            UserProfile_record.email         = user_record.email
            UserProfile_record.dob           = user_record.dob
            UserProfile_record.mobile_number = user_record.mobile_number
            UserProfile_record.save()
            return HttpResponseRedirect('/seller/profile')

        else:
            return render(request, 'seller/edit_profile.html', {'form': form,'user_record': user_record }, )
    else:
        form = EditProfileForm()
        return render(request, 'seller/edit_profile.html', {'form': form,'user_record': user_record}, )
