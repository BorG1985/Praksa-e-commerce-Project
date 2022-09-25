from audioop import add
from base64 import urlsafe_b64decode
from unicodedata import name
from django import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views
from .views import SearchResultsView
urlpatterns = [
    path('', views.base, name="base"),
    path('homepage', views.homePage, name="homepage"),
    path('local-stores', views.local_stores, name="local-stores"),
    path('log-in', views.log_in, name="log-in"),
    path('sign-in', views.sign_in, name="sign-in"),
    path('admin-login', views.admin_login, name="admin-login"),
    path('lookbook', views.lookbook, name="lookbook"),
    path('product-view', views.productView, name="product-view"),
    path('mens', views.mens, name="mens"),
    path('womens', views.womens, name="womens"),
    path('your-lookbook', views.your_lookbook, name="your-lookbook"),
    path('header', views.header, name="header"),
    path('footer', views.footer, name="footer"),
    path('cart', views.cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('make_order', views.make_order, name='make_order'),
    path('finish_order', views.finish_order, name='finish_order'),
    path("choose-hat", views.choose_hat, name="choose-hat"),
    path("choose-shirt", views.choose_shirt, name="choose-shirt"),
    path("choose-jeans", views.choose_jeans, name="choose-jeans"),
    path("choose-shoes", views.choose_shoes, name="choose-shoes"),
    path("add_to_lookbook", views.add_to_lookbook, name='add_to_lookbook'),
    path('finish_order', views.finish_order, name='finish_order'),
    path("filter_products", views.filter_products, name='filter_products'),
    path('account/', include('account.urls')),
    path("log_out", views.log_out, name='log_out'),
    path("user_info",views.user_info,name='user_info'),
    path('search-results', SearchResultsView.as_view(), name="search-results"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
