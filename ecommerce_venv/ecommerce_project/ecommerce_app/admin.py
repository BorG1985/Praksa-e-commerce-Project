from atexit import register
from django.contrib import admin
from .models import NewUser, Product, Profile, Category, TShirt, Jeans,Color, ProductSize

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Jeans)
admin.site.register(TShirt)
admin.site.register(Color)
admin.site.register(ProductSize)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('status', 'gender', 'product_title', 'number_of_products',
                    'product_price', 'size', 'color', 'product_image', 'slug')
    list_display_links = ['color', ]
    list_filter = ('gender', 'status', 'product_title', 'product_price')
    list_editable = ['gender', 'number_of_products',
                     'product_price', 'status', 'size']
    search_fields = ('product_title', 'product_price')
    prepopulated_fields = {'slug': ('product_title', )}


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
