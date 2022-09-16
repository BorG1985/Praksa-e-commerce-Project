from .models import Cart, LocalStores,CurrentSession


def add_variable_to_context(request):
    number_of_products = Cart.objects.all().count()
    current_user_value=CurrentSession.objects.all().count()
    if current_user_value > 0:
        curent_user=CurrentSession.objects.all().order_by('-id').values_list()[:1]
        current_user=curent_user[0][1]
    else:
        current_user=""
    
    
    return {
        'number_of_products': number_of_products,
        'current_user':  current_user,
    }


def customer_support(request):
    return {
        'customer_support': LocalStores.objects.all(),
    }
