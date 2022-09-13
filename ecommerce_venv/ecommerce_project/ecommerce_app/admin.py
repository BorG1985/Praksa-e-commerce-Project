from atexit import register
from django.contrib import admin
from .models import NewUser, Product, Category, TShirt, Jeans, Color, ProductSize, LocalStores

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Jeans)
admin.site.register(TShirt)
admin.site.register(Color)
admin.site.register(ProductSize)
admin.site.register(LocalStores)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['status', 'gender', 'product_title', 'product_price',
                    'size', 'color', 'product_image', 'tag_list', 'slug']  # tag_list vraca tags polje
    list_display_links = ['color', ]
    list_filter = ('gender', 'status', 'product_title',
                   'product_price')
    list_editable = ['gender', 'product_price', 'status', 'size']
    search_fields = ('product_title', 'product_price')
    prepopulated_fields = {'slug': ('short_product_description', )}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
