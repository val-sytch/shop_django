from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from carton.cart import Cart
from djog.models.model_dogs import Dogs


def add(request, id):
    cart = Cart(request.session)
    product = Dogs.objects.get(id=id)
    cart.add(product, price=product.price)
    message = 'The dog was added to the cart'
    return HttpResponseRedirect(reverse('index'), message)


# def add_to_cart(request, id):
#     cart = Cart(request.session)
#     cat = Cat.objects.get(id=id)
#     if cat not in cart:
#         cart.add(cat, price=cat.price)
#         message = 'Cat was added to shopping cart'
#     else:
#         message = 'Cat already in the shopping cart'
#     if 'cat' in request.path:
#         return HttpResponseRedirect(reverse('cat'), message)
#     else:
#         return HttpResponseRedirect(
#             '{}?status_message={}'.format(reverse('cats_shop:index'),
#                                           message))


def remove(request, id):
    cart = Cart(request.session)
    product = Dogs.objects.get(id=id)
    cart.remove(product)
    message = 'The dog was removed from the cart'
    return HttpResponseRedirect(reverse('cart:shopping-cart-show'), message)


def show(request):
    return render(request, 'shopping/show-cart.html')
