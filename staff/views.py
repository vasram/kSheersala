# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from seller.models import *
from seller.forms import *
import json

def index(request):
    return HttpResponse("You're at the staff index.")

def register(request):
    # if any user already login
    if request.user.is_authenticated():
        username = request.user.username
        if len(Staff_Record.objects.filter(username=username)) != 0:
            return HttpResponseRedirect('/staff/home/')
        elif len(Sellers_Records.objects.filter(username=username)) != 0:
            return HttpResponseRedirect('/seller/home/')
    context = RequestContext(request)
    registered = False

     # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
            staff_form = StaffForm(data=request.POST)
            # check if already registered
            username = staff_form['username'].value()
            if len(User.objects.filter(username=username)) != 0:
                message = 'An account already exists with this username !'
                return render(request, 'staff/register.html',  {'staff_form': staff_form,'message': message, })
            if staff_form.is_valid() and len(Staff_Record.objects.filter(username=username)) != 0:
                user = staff_form.save()
                user.set_password(user.password)
                user.save()
                registered = True
                return HttpResponseRedirect('/staff/login/')
            else:
                message = 'Username  not available, Please Enter Correct Username or contact Admin   !'
                return render(request, 'staff/register.html', {'staff_form': staff_form, 'message': message, })
    else:
            staff_form = StaffForm()
            return render(request,'staff/register.html',{'staff_form': staff_form,  'registered': registered})




def staff_login(request):
    # if any user already login
    if  request.user.is_authenticated():
        username = request.user.username
        #user_record = Staff_Record.objects.get(username=username)
        if len(Staff_Record.objects.filter(username=username)) != 0:
           return HttpResponseRedirect('/staff/home/')
        else:
            return HttpResponseRedirect('/seller/home/')

    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        #user_record = Staff_Record.objects.get(username=username)
        if user is not None and len(Staff_Record.objects.filter(username=username)) != 0:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/staff/home/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            #print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponseRedirect('/staff/try_login_again/')
    else:
        return render(request,'staff/login.html', {})


@login_required(login_url='/staff/login/')
def staff_home(request):
  username = request.user.username
  if len(Staff_Record.objects.filter(username=username)) != 0:
      user_record = Staff_Record.objects.get(username=username)
      return render(request, 'staff/base.html', {'user_record': user_record}, )
  else:
       return HttpResponseRedirect('/seller/home/')

def try_login_again(request):
    return HttpResponse("<p>  User not exits , try again , Please give correct user name and password  .. "
                        "</br>"
                        "<a href='/staff/login/'>LOGIN</a>"
                        "</p>")


@login_required(login_url='/staff/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required (login_url='/staff/login/')
def staff_profile(request):
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    return render(request,'staff/profile.html',{'user_record': user_record},)



def edit_profile(request):
    context = RequestContext(request)
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    form = StaffEditProfileForm(request.POST or None, initial={'first_name':user_record.first_name, 'last_name':user_record.last_name , 'address':user_record.address,'email':user_record.email,'mobile_number':user_record.mobile_number,'dob':user_record.dob})
    if request.method == 'POST':
        if form.is_valid():
            #For Seller_Record Update
            user_record.first_name = request.POST['first_name']
            user_record.last_name = request.POST['last_name']
            user_record.address = request.POST['address']
            user_record.email = request.POST['email']
            user_record.mobile_number = request.POST['mobile_number']
            user_record.dob = request.POST['dob']
            user_record.save()
            #Users Update
            User_record = User.objects.get(username=username)
            User_record.first_name = user_record.first_name
            User_record.last_name = user_record.last_name
            User_record.save()
            # seller UserProfile Update
            return HttpResponseRedirect('/staff/profile')
        else:
            return render(request, 'staff/edit_profile.html', {'form': form,'user_record': user_record }, )
    else:
        form = StaffEditProfileForm()
        return render(request, 'staff/edit_profile.html', {'form': form,'user_record': user_record}, )

def calculate_price(quantity, Fat, SNF):
    UpdatePrice =  Milk_rate.objects.order_by("up_date")[:1]
    for first in UpdatePrice:
       x = first.Kg_Fat_Rate
       y = first.Kg_SNF_Rate
    payment = float(quantity) * ((float(x) * float(Fat)) + (float(y) * float(SNF)))
    return payment


def compute_payment(request):
    quantity      = request.GET['quantity']
    Fat           = request.GET['Fat']
    SNF           = request.GET['SNF']

    payment = calculate_price(quantity,Fat,SNF)



def dailyTransactions(request):
    context = RequestContext(request)
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    message = 'not insert'
    if request.method == 'POST':
        transactions_form = Daily_transactionsForm(data=request.POST)
        username1 = transactions_form['username'].value()
        quantity = request.POST['quantity']
        Fat = request.POST['Fat']
        SNF = request.POST['SNF']

        payment = calculate_price(quantity, Fat, SNF)

        if transactions_form.is_valid() and len(Sellers_Records.objects.filter(username=username1)) != 0:

           #transactions = transactions_form.save()
           user_record1 = Sellers_Records.objects.get(username=username1)
           t_username        = transactions_form['username'].value()
           t_quantity        = transactions_form['quantity'].value()
           t_Fat             = transactions_form['Fat'].value()
           t_SNF             = transactions_form['SNF'].value()
           t_cattle          = transactions_form['cattle'].value()
           t_transaction_date = transactions_form['transaction_date'].value()
           t_payment1         = payment

           record = Daily_transactions(username = t_username,
                                       quantity =  t_quantity,
                                       Fat      = t_Fat,
                                       SNF      = t_SNF,
                                       cattle   = t_cattle,
                                       transaction_date = t_transaction_date,
                                       payment  = t_payment1
                                       )
           record.save()
           return render(request, 'staff/payment.html', {'transactions_form':transactions_form,'payment':payment,'user_record': user_record,}, )
        else:
            return render(request, 'staff/dailytransactions.html', {'transactions_form':transactions_form,'user_record': user_record,'message':message}, )
    else:
        transactions_form= Daily_transactionsForm()
        return render(request, 'staff/dailytransactions.html', {'transactions_form':transactions_form ,'user_record': user_record}, )

def payment(request):
    return render(request, 'staff/payment.html', {})


def alltransactionshistory(request):
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    transactions_record = Daily_transactions.objects.all().order_by("-transaction_id")[:10]
    return render(request, 'staff/transactions.html', {'transactions_record': transactions_record ,'user_record':user_record }, )

def getseller (request):
    get_all = Sellers_Records.objects.all()
    context = RequestContext(request)
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    message = 'This username not exists !'
    if request.method == 'POST':
        username1 = request.POST['username']
        #if getseller_form.is_valid():
        if len(Sellers_Records.objects.filter(username=username1)) != 0:
           user_record1 = Sellers_Records.objects.get(username=username1)
           return render(request, 'staff/seller_profile.html', {'user_record1': user_record1,'user_record': user_record}, )
          # return HttpResponseRedirect('/staff/dailytransactions/')
        else:
            getseller_form = Get_seller_usernameForm()
            return render(request, 'staff/Get_seller.html',
                          {'getseller_form': getseller_form, 'user_record': user_record,'message':message,'get_all':get_all}, )
    else:
        getseller_form= Get_seller_usernameForm()
        return render(request, 'staff/Get_seller.html', {'getseller_form': getseller_form,'user_record': user_record,'get_all':get_all}, )






def delete_seller_record(request):

    if request.method == 'GET':

        username = request.GET['username']
        #delete from Seller_Records
        record = Sellers_Records.objects.get(username=username)
        record.delete()
        #delete from User
        user_record = User.objects.get(username=username)
        user_record.delete()

        data = {'mesg': "Success!"}
        return HttpResponse(json.dumps(data))

    else:
        HttpResponseRedirect('/staff/home/')




def update_seller_record(request):
    context = RequestContext(request)
    if request.method == 'GET':

        username = request.GET['username']
        #delete from Seller_Records
        record = Sellers_Records.objects.get(username=username)
        form = EditProfileForm(request.POST or None, initial={'first_name':user_record.first_name, 'last_name':user_record.last_name , 'address':user_record.address,'email':user_record.email,'dob':user_record.dob})
        # username1 = EditProfileForm['username'].value()

        if form.is_valid():
            #For Seller_Record Update
            user_record.first_name = request.GET['first_name']
            user_record.last_name = request.GET['last_name']
            user_record.address = request.GET['address']
            user_record.email = request.GET['email']
            user_record.dob = request.GET['dob']
            user_record.save()

            #Users Update

            User_record = User.objects.get(username=username)
            User_record.first_name = user_record.first_name
            User_record.last_name = user_record.last_name
            User_record.save()

            # seller UserProfile Update
            UserProfile_record = UserProfile.objects.get(user__username=request.user.username)
            UserProfile_record.address = user_record.address
            UserProfile_record.first_name = user_record.first_name
            UserProfile_record.last_name = user_record.last_name
            UserProfile_record.address=user_record.address
            UserProfile_record.email = user_record.email
            UserProfile_record.dob = user_record.dob
            UserProfile_record.save()
            return HttpResponseRedirect('/staff/home')

        else:
            return render(request, 'seller_edit_profile.html', {'form': form }, )
    else:
        form = EditProfileForm()
        return render(request, 'seller_edit_profile.html', {'form': form}, )

"""
def remove_items(request):
    if request.method == 'POST':
        form = DeleteForm()
        
        username1 = request.POST.get('username')
        user_record = Sellers_Records.objects.get(username=username)
        user_record .delete()
        """


def review(request):
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    review_record = Review.objects.all().order_by("-date")[:25]
    return render(request, 'staff/review.html',
                  {'review_record': review_record, 'user_record': user_record}, )



def milk_price(request):
    username = request.user.username
    user_record = Staff_Record.objects.get(username=username)
    milk_record = Milk_rate.objects.all().order_by("-up_date")[:10]
    return render(request, 'staff/milk_price.html',
                      {'milk_record': milk_record, 'user_record': user_record}, )
