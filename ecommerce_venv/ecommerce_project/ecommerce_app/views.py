
# Create your views here.
from locale import currency
from operator import countOf
import re
from typing import NoReturn
from django.db.models.query import EmptyQuerySet
from django.http import request, HttpResponse
from django.http.response import HttpResponseRedirect
import mysql.connector
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile, NewUser, Product
from ecommerce_app.models import Cart, AllOrders, OrderValues
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
import mysql.connector
from datetime import date, datetime, timedelta

today = date.today()
now = datetime.now()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce"


)


mycursor = mydb.cursor()


def base(request):

    return render(request, 'base.html')


def homePage(request):
    return render(request, 'homepage.html')


def header(request):

    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html', )


def localStores(request):
    return render(request, 'local-stores.html')


def productView(request):
    return render(request, 'product-view.html')


def lookbook(request):
    return render(request, 'lookbook.html')


def signIn(request):  # rename to register
    if request.method == "POST":
        signin_form = UserRegistrationForm(request.POST)
        if signin_form.is_valid():
            signin_form.save()
            return HttpResponseRedirect('sign-in')
    else:
        signin_form = UserRegistrationForm()
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        res = NewUser.objects.filter(email=email, password=password).count()

        if (res != 0):

            # Redirect to a success page.
            return HttpResponse("Proradio materi")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("Ne radi")
    else:
        login_form = LoginForm()

    return render(request, 'sign-in.html', {"signin_form": signin_form, "login_form": login_form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register_done(request):
    return render(request, 'account/register_done.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['Password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'log-in.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def mens(request):
    on_count = Product.objects.filter(status="on_count")
    off_count = Product.objects.filter(status="off_count")

    return render(request, 'mens.html', {'on_count': on_count, 'off_count': off_count, })


def cart(request):
    product = Cart.objects.all()
    return render(request, 'cart.html', {'cart': product})


num = []


def add_to_cart(request):
    if request.method == "POST":
        id = request.POST['id']

        mydata = Product.objects.filter(id=id).values()

        values_by_id = {
            'mymembers': mydata,
        }
        b = values_by_id['mymembers'][0]

        order_number = 1
        num.append(order_number)
        i = len(num)
        n_order_number = i + 1
        Cart(order_number=order_number, order_product=b['product_title'], order_product_price=b[
             'product_price'], order_product_Value="$", order_product_image=b['product_image']).save()
        AllOrders(order_number=n_order_number, order_product_id=b['id'], order_product=b['product_title'],
                  order_product_price=b['product_price'], order_product_Value="$", order_product_image=b['product_image']).save()

        on_count = Product.objects.filter(status="on_count")
        off_count = Product.objects.filter(status="off_count")
        number_of_items = Cart.objects.all().count()

        return render(request, 'mens.html', {'on_count': on_count, 'off_count': off_count, "number_of_items": number_of_items})


def make_order(request):
    Cart.objects.all().delete()
    if request.method == "POST":
        price = request.POST['total_value']
        return render(request, 'payment.html', {"price": price})


def finish_order(request):
    if request.method == "POST":
        card_number = request.POST['card']
        name = request.POST['name']
        expiration_date = request.POST['expiration']
        security_code = request.POST['security']
        price = request.POST['price']
        date = today.strftime("%m/%d/%y")
        time = now.strftime("%H:%M:%S")
        sql = "select * from ecommerce_all_orders ORDER BY id DESC LIMIT 1;"

        mycursor.execute(sql)
        a = mycursor.fetchall()
        order_number = a[0][1]
        products = []
        mydata = AllOrders.objects.filter(order_number=order_number).values()

        values_by_id = {
            'mymembers': mydata,
        }
        b = values_by_id['mymembers']
        for i in b:
            products.append(i['order_product_id'])
        products1 = ';'.join(products)

        OrderValues(order_number=order_number, Price=price, Name=name, card_number=card_number,
                    expiration_date=expiration_date, security_code=security_code, date=date, time=time, Products=products1).save()

        return render(request, 'payment.html', {"products": products1})
