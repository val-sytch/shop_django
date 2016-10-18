from django.http import HttpResponseRedirect
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

def remove(request, id):
    cart = Cart(request.session)
    product = Dogs.objects.get(id=id)
    cart.remove(product)
    message = 'The dog was removed from the cart'
    return HttpResponseRedirect(reverse('cart:shopping-cart-show'), message)

def show(request):
    return render(request, 'shopping/show-cart.html')
