from django.shortcuts import render,redirect
from store.models import Product
from .models import Carts, CartsItem

# Create your views here.

from django.http import HttpResponse

def _carts_id(request):
    carts = request.session.session_key
    if not carts:
         carts = request.session.create()
    return carts
def add_carts(request, product_id):
    product = Product.objects.get(id = product_id) # get the products
    try:
        carts = Carts.objects.get(carts_id=_carts_id(request)) # get the cart using the cart_id present sesion
    except Carts.DoesNotExist:
        carts = Carts.objects.create(
            carts_id = _carts_id(request)
        )
    carts.save()

    try:
        carts_item = CartsItem.objects.get(product=product, carts=carts)
        carts_item.quantity += 1 # Cart_item_quantity = cart_ime.quantity + 1
        carts_item.save() 
    except CartsItem.DoesNotExist:
        carts_item = CartsItem.objects.create(
            product = product,
            quantity = 1, 
            carts = carts,

        )
        carts_item.save()

    return redirect('carts')


def carts(request, total=0, quantity=0, carts_items=None):
    try:
        carts = Carts.objects.get(carts_id = _carts_id(request))
        carts_items = CartsItem.objects.filter(carts=carts, is_active=True)
        for carts_item in carts_items:
            total += (carts_item.product.price * carts_item.quantity)
            quantity += carts_item.quantity
    except ObjectNotExist:
        pass #just ignore

    context = {
        'total':total,
        'quantity': quantity,
        'carts_items': carts_items,
        }


    return render(request, 'store/cart.html', context)