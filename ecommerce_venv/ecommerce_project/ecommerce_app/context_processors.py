from .models import Cart, LocalStores


def add_variable_to_context(request):
    number_of_products = Cart.objects.all().count()
    return {
        'number_of_products': number_of_products,
    }


def customer_support(request):
    return {
        'customer_support': LocalStores.objects.all(),
    }
