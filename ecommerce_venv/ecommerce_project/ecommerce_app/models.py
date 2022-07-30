# Create your models here.
from pyexpat import model
from re import L
from django.conf import settings
from distutils.command.upload import upload
from tabnanny import verbose
from tkinter import Widget
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.db import connections
from django import forms
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
from django import forms
from PIL import Image


class NewUser(models.Model):
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=50, null=False, blank=False)
    password2 = models.CharField(max_length=50, null=True, blank=False)

    class Meta:
        db_table = "ecommerce_newuser"
        verbose_name = "New user"
        verbose_name_plural = "New users"

    def __str__(self):
        return self.email


class ProductColour(models.Model):
    red = models.CharField(max_length=3, default="Red")
    blue = models.CharField(max_length=4, default="Blue")
    green = models.CharField(max_length=5, default="Green")
    black = models.CharField(max_length=5, default="Black")
    orange = models.CharField(max_length=6, default="Orange")
    yellow = models.CharField(max_length=6, default="Yellow")

    class Meta:
        verbose_name = "Colour"
        verbose_name_plural = "Colours"


STATUS_CHOICES = (
    ('on_count', 'On count'),
    ('off_count', 'Off count'),
)
GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
)
COLOR_CHOICES = (
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('orange', 'Orange'),
)

UPPER_BODY_SIZE_CHOICES = (
    ('xxs', 'XXS'),
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
)
LOWER_BODY_SIZE_WIDTH_CHOICES = (
    ('skinny', 'Skinny'),
    ('slim', 'Slim'),
    ('regular', 'Regular'),
    ('wide', 'Wide')
)
LOWER_BODY_SIZE_HEIGHT_CHOICES = [
    ('Mens', (
        ('xxs', 'UK 26; Europe 42; USA 26; International XXS'),
        ('xs', 'UK 28; Europe 44; USA 28; International XS'),
        ('s', 'UK 30; Europe 46; USA 30; International S'),
        ('m', 'UK 32; Europe 48; USA 32; International M'),
        ('l', 'UK 34; Europe 50; USA 34; International L'),
        ('xl', 'UK 36; Europe 52; USA 36; International XL'),
        ('xxl', 'UK 38; Europe 54; USA 38; International XXL'),
        ('xxxl', 'UK 40; Europe 56; USA 40; International XXL'),

    )
    ),

    ('Women', (
        ('xxs', 'UK 24; Europe 40; USA 24; International XXS'),
        ('xs', 'UK 26; Europe 42; USA 26; International XS'),
        ('s', 'UK 38; Europe 44; USA 38; International S'),
        ('m', 'UK 30; Europe 46; USA 30; International M'),
        ('l', 'UK 32; Europe 48; USA 32; International L'),
        ('xl', 'UK 34; Europe 50; USA 34; International XL'),
        ('xxl', 'UK 36; Europe 52; USA 36; International XXL'),
        ('xxxl', 'UK 38; Europe 54; USA 38; International XXL'),
    )
    ),
    ('Child', (
        ('1 - 12 months', '1 - 12 months'),
        ('1 - 2 years', '1 - 2 years'),
        ('2 - 3 years', '2 - 3 years'),
        ('3 - 4 years', '3 - 4 years'),
        ('4 - 5 years', '4 - 5 years'),
        ('5 - 6 years', '5 - 6 years'),
        ('6 - 7 years', '6 - 7 years'),
        ('7 - 8 years', '7 - 8 years'),
        ('8 - 9 years', '8 - 9 years'),
        ('9 - 10 years', '9 - 10 years'),
        ('10 - 11 years', '10 - 11 years'),
        ('11 - 12 years', '11 - 12 years'),
        ('12 - 13 years', '12 - 13 years'),
        ('13 - 14 years', '13 - 14 years'),
    )
    ),
    ('unknown', 'Unknown'),
]


class ProductSize(models.Model):
    xxs = models.PositiveIntegerField()
    xs = models.PositiveIntegerField()
    m = models.PositiveIntegerField()
    l = models.PositiveIntegerField()
    xl = models.PositiveIntegerField()
    xxl = models.PositiveIntegerField()


class Color(models.Model):
    red = models.PositiveIntegerField()
    green = models.PositiveIntegerField()
    orange = models.PositiveIntegerField()


class TShirt(models.Model):
    manufacturer = models.CharField(max_length=30, default=None)
    model = models.CharField(max_length=30, default=None)
    size = models.CharField(
        max_length=3, choices=UPPER_BODY_SIZE_CHOICES, null=True, blank=True)
    NO_of_availabile_products = models.ForeignKey(
        ProductSize, on_delete=models.CASCADE)
    NO_of_availabile_colors = models.ForeignKey(
        Color, on_delete=models.CASCADE)


class Jeans(models.Model):
    manufacturer = models.CharField(max_length=30, default=None)
    model = models.CharField(max_length=30, default=None)
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    width = models.CharField(
        max_length=15, choices=LOWER_BODY_SIZE_WIDTH_CHOICES)
    height = models.CharField(
        max_length=15, choices=LOWER_BODY_SIZE_HEIGHT_CHOICES)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    product_title = models.CharField(
        max_length=100, db_index=True, null=False, blank=False)
    number_of_products = models.PositiveIntegerField(null=False, blank=False)
    product_description = models.TextField(blank=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICE, null=True)
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(
        upload_to="products/", null=True, blank=True)
    # models.CharField(max_length=10, choices=COLOR_CHOICES, default="red")
    color = models.OneToOneField(ProductColour, on_delete=models.CASCADE)
    # models.CharField(max_length=6, choices=SIZE_CHOICES, null=False, blank=False)
    size = models.OneToOneField(ProductSize, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='off_count')
    slug = models.SlugField(
        max_length=250, null=False, unique=True, db_index=True, blank=False)

    class Meta:
        ordering = ('product_title',)
        index_together = (('id', 'slug'),)
        db_table = "ecommerce_product"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        app_label = "ecommerce_app"

    def __str__(self):
        return f'{self.product_title, self.product_price, self.status}'


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True)

    class Meta:
        db_table = "ecommerce_profile"
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Cart(models.Model):
    order_number = models.IntegerField()
    order_product = models.CharField(max_length=100)
    order_product_price = IntegerField()
    order_product_value = CharField(max_length=100)
    order_product_image = models.ImageField(
        upload_to="products/", blank=True)

    class Meta:
        db_table = "ecommerce_order"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class AllOrders(models.Model):
    order_number = models.IntegerField()
    order_product = models.CharField(max_length=100)
    order_product_id = models.CharField(max_length=50)
    order_product_price = IntegerField()
    order_product_value = CharField(max_length=100)
    order_product_image = models.ImageField(
        upload_to="products/", blank=True)

    class Meta:
        db_table = "ecommerce_all_orders"
        verbose_name_plural = "All orders"


class OrderValues(models.Model):
    order_number = models.IntegerField()
    products = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    card_number = models.BigIntegerField()
    expiration_date = models.CharField(max_length=50)
    security_code = models.IntegerField()
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=10)

    class Meta:
        db_table = "ecommerce_order_values"
        verbose_name_plural = "Order values"
