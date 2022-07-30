from .models import Cart
def add_variable_to_context(request):
    number_of_products=Cart.objects.all().count()
    return {
         'number_of_products' : number_of_products
     }
