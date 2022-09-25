
# Create your views here.
from audioop import reverse
from email import message
from locale import currency
from operator import countOf
import re
from typing import NoReturn
from unicodedata import name
from django.db.models.query import EmptyQuerySet
from django.http import request, HttpResponse
from django.http.response import HttpResponseRedirect
import mysql.connector
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import NewUser, Product, ProductSize
from ecommerce_app.models import Cart, AllOrders, OrderValues, CurrentLookbook, LocalStores, UserSession, CurrentSession
from .forms import LoginForm, UserRegistrationForm, UserEditForm
import mysql.connector
from datetime import date, datetime, timedelta
from taggit.models import Tag
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.list import ListView
import bcrypt

today = date.today()
now = datetime.now()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
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
    customer_support = LocalStores.objects.all()
    return render(request, 'footer.html', {'customer_support': customer_support})


def local_stores(request):
    local_stores = LocalStores.objects.all()
    return render(request, 'local-stores.html', {'local_stores': local_stores})


def productView(request):

    if request.method == "POST":
        id = request.POST['id']
        product = Product.objects.filter(id=id)
        quantity = ProductSize.objects.values_list('l', flat=True).distinct()
        tags = Tag.objects.all()

        return render(request, 'product-view.html', {"product": product, "quantity": quantity, "tags": tags})


def lookbook(request):
    return render(request, 'lookbook.html')


def admin_login(request):
    login_form = LoginForm()
    if request.method == "POST":
        mail = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=mail, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("homepage")
        else:
            return HttpResponse("nije nasao usera")
    login_form = LoginForm()
    return render(request, 'admin-sign-in.html', {"login_form": login_form})


# --> sredjen user_sign_in_and_login jos samo responesi da budu lijepi

def log_in(request):
    login_form = LoginForm(request.POST)
    if request.method == "POST":
        email = request.POST['email']
        password = str(request.POST['password'])
        if login_form.is_valid():
            user_login_pass = password.encode('utf-8')
        
        
            counter=NewUser.objects.filter(email=email).count()
            if counter > 0:
                user_email_row=NewUser.objects.filter(email=email).values_list()
                user_pass=user_email_row[0][2]
                user_passs=user_pass.encode()
                
                result=bcrypt.checkpw(user_login_pass,user_passs)
            
            if result== True:
                user_exist = NewUser.objects.filter(
                    email=email).get()
                
                UserSession(username=email,session_started=now.strftime("%H:%M:%S"),session_started_date=today.strftime("%m/%d/%y")).save()
                CurrentSession(username=email).save()
                # http response prihvata samo str value i zato formatiranje
                return render(request,'base.html')
            else:
                return HttpResponse("ne cackaj formu")
        else:
            login_form = LoginForm()
            """UserSession(username=email,session_started=now.strftime("%H:%M:%S"),session_started_date=today.strftime("%m/%d/%y")).save()
            CurrentSession(username=email).save()
            return render(request,'homepage.html')"""
    return render(request, 'log-in.html', {"login_form": login_form})


def sign_in(request):
    signin_form = UserRegistrationForm(request.POST)
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        name=request.POST['name']
        surname=request.POST['surname']
        address=request.POST['address']
        phone=request.POST['phone_number']
        bytes = password.encode('utf-8')
        bytes2 = password2.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_pass1 = bcrypt.hashpw(bytes, salt)
        hashed_pass2 = bcrypt.hashpw(bytes2, salt)
        encode_pass1=hashed_pass1.decode()
        encode_pass2=hashed_pass2.decode()


        if password == password2:
            if signin_form.is_valid():
                new_user = NewUser.objects.create(
                    email=email, password=encode_pass1, password2=encode_pass2,name=name,surname=surname,addres=address,phone=phone)  # provjeriti da li imaju dva ista mail u bazi!!!
                print("kreiran user")
                login_form = LoginForm(request.POST)
                
                # http response prihvata samo str value i zato formatiranje
                return render(request,'log-in.html' , {"login_form": login_form})
            else:
                messages.error(request, "ne valja ti nesto")
                signin_form = UserRegistrationForm()
        else:
            return HttpResponse("Password dont match, please try again!")
    else:
        signin_form = UserRegistrationForm()

    return render(request, 'sign-in.html', {"signin_form": signin_form})


def mens(request):
    men_products = Product.objects.filter(gender="male", status="on_count")
    on_count = Product.objects.filter(status="on_count")
    off_count = Product.objects.filter(status="off_count")
    paginator = Paginator(men_products, 12)  # Show 12 products per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'mens.html', {'on_count': on_count, 'off_count': off_count, 'page_obj': page_obj, 'men_products': men_products})


def womens(request):
    women_products = Product.objects.filter(gender="female", status="on_count")
    on_count = Product.objects.filter(status="on_count")
    off_count = Product.objects.filter(status="off_count")
    paginator = Paginator(women_products, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'womens.html', {'on_count': on_count, 'off_count': off_count, 'page_obj': page_obj, 'women_products': women_products})


def your_lookbook(request):
    product = Product.objects.all()[:1]
    return render(request, 'your-lookbook.html', {'product': product})


def cart(request):
    product = Cart.objects.all()
    return render(request, 'cart.html', {'cart': product})


num = []


def add_to_cart(request):
    counter=OrderValues.objects.all().count()
    if request.method == "POST":
        id = request.POST['id']
        size="XS"

        mydata = Product.objects.filter(id=id).values()

        values_by_id = {
            'mymembers': mydata,
        }
        b = values_by_id['mymembers'][0]
        
        if counter > 0 :
            order__number=OrderValues.objects.all().order_by('-id').values_list()[:1]
            order_number=order__number[0][1]
        else:
            order_number=0


        
        Cart(order_product_id=id,order_product_size=size,order_number=order_number + 1, order_product=b['product_title'], order_product_price=b[
             'product_price'], order_product_value="$", order_product_image=b['product_image']).save()
        AllOrders(order_product_size=size,order_number=order_number + 1, order_product_id=b['id'], order_product=b['product_title'],
                  order_product_price=b['product_price'], order_product_value="$", order_product_image=b['product_image']).save()

        on_count = Product.objects.filter(status="on_count")
        off_count = Product.objects.filter(status="off_count")
        
        response = redirect('mens')
        return response


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
        
        email=CurrentSession.objects.all().order_by('-id').values_list()[:1]
        counter=OrderValues.objects.all().count()
        if counter > 0 :
            order__number=OrderValues.objects.all().order_by('-id').values_list()[:1]
            order_number=order__number[0][1]
        else:
            order_number=1
        

        
        products = []
        mydata = AllOrders.objects.filter(order_number=order_number + 1).values()

        values_by_id = {
            'mymembers': mydata,
        }
        b = values_by_id['mymembers']
        for i in b:
            products.append(i['order_product_id'])
        products1 = ';'.join(products)

        OrderValues(order_number=order_number + 1, price=price, name=name, card_number=card_number,
                    expiration_date=expiration_date, security_code=security_code, date=date, time=time, products=products1,username=email[0][1]).save()

        return render(request, 'payment.html', {"products": products1})


def choose_hat(request):
    product = Product.objects.filter(category="hats")
    return render(request, "lookbook-choose.html", {"product": product})


def choose_shirt(request):
    product = Product.objects.filter(category="shirts")
    return render(request, "lookbook-choose.html", {"product": product})


def choose_jeans(request):
    product = Product.objects.filter(category="jeans")
    return render(request, "lookbook-choose.html", {"product": product})


def choose_shoes(request):
    product = Product.objects.filter(category="shoes")
    return render(request, "lookbook-choose.html", {"product": product})


def add_to_lookbook(request):
    if request.method == "POST":
        id = request.POST['id']
        mydata = Product.objects.filter(id=id).values()

        values_by_id = {
            'mymembers': mydata,
        }
        b = values_by_id['mymembers'][0]
        CurrentLookbook(
            product_id=b['id'], lookbook_image=b['product_image'], product_category=b['category']).save()
        product_hat = CurrentLookbook.objects.filter(
            product_category="hats").last()
        product_shirt = CurrentLookbook.objects.filter(
            product_category="shirts").last()
        product_jeans = CurrentLookbook.objects.filter(
            product_category="jeans").last()
        product_shoes = CurrentLookbook.objects.filter(
            product_category="shoes").last()
        return render(request, 'your-lookbook.html', {"product_hat": product_hat, "product_shirt": product_shirt, "product_jeans": product_jeans, "product_shoes": product_shoes})


def filter_products(request):
    if request.method == "POST":

        color = request.POST['color-filter']
        gender = request.POST['gender-filter']

        on_count = Product.objects.filter(
            status="on_count", color=color, gender=gender)
        count = Product.objects.filter(status="on_count", color=color).count()
        if count == 0:
            messages.success(
                request, "Nažalost,trenutno nemamo proizvoda koji odgovaraju filteru")
        return render(request, 'mens.html', {'page_obj': on_count})



def log_out(request):
    CurrentSession.objects.all().delete()
    return render(request,'base.html')

    
def user_info(request):
    info=OrderValues.objects.all()
    email=CurrentSession.objects.all().order_by('-id').values_list()[:1]
    
    account_info=NewUser.objects.filter(email=email[0][1])
    return render(request,'user.html',{"info":info,"account_info":account_info})

def remove_button(request):
    if request.method == "POST":
        id=request.POST['id']
        size=request.POST['sizes']
        Cart.objects.filter(order_product_id=id,order_product_size=size).delete()
        response = redirect('cart')
        return response



class SearchResultsView(ListView):
    model = Product
    template_name = "search-results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(product_title__icontains=query) | Q(
                long_product_description__icontains=query)
        )
        return object_list
