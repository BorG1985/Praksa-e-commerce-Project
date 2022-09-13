
# Create your views here.
from audioop import reverse
from email import message
from locale import currency
from operator import countOf
import re
from typing import NoReturn
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
    user_exist = NewUser.objects.filter(
        email=email, password=password).get()
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
        password = request.POST['password']
        if login_form.is_valid():
            user_exist = NewUser.objects.filter(
                email=email, password=password).exists()  # exists() vraca True ili False
            if user_exist == False:
                # \"ide u navodnike\"
                return HttpResponse(f"User with email: \"" + str(email) + "\" does not exist or wrong e-mail and password!")
            if user_exist is not None:
                user_exist = NewUser.objects.filter(
                    email=email, password=password).get()
                registered_user = user_exist
                # http response prihvata samo str value i zato formatiranje
                return HttpResponse(f"Welcome \"" + str(user_exist)+"\"")
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
        if password == password2:
            if signin_form.is_valid():
                new_user = NewUser.objects.create(
                    email=email, password=password, password2=password2)  # provjeriti da li imaju dva ista mail u bazi!!!
                print("kreiran user")
                signin_form.save()
                # http response prihvata samo str value i zato formatiranje
                return HttpResponse(f"Welcome" + " "+str(new_user))
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
             'product_price'], order_product_value="$", order_product_image=b['product_image']).save()
        AllOrders(order_number=n_order_number, order_product_id=b['id'], order_product=b['product_title'],
                  order_product_price=b['product_price'], order_product_value="$", order_product_image=b['product_image']).save()

        on_count = Product.objects.filter(status="on_count")
        off_count = Product.objects.filter(status="off_count")
        number_of_items = Cart.objects.all().count()
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
