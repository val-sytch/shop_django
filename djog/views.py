from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . models.model_dogs import Dogs
from . models.model_orders import Orders
from . forms import OrderForm
from carton.cart import Cart

def index(request):
    dogs_list = Dogs.objects.all()
    context = {
        'dogs_list': dogs_list
    }
    return render(request, 'djog/index.html', context)

def login(request):
    return render(request, 'djog/login.html')

def logout(request):
    return render(request, 'djog/logout.html')

def register(request):
    return render(request, 'djog/register.html')

def order(request):
    return render(request, 'djog/order.html')

def order_make(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            cart = Cart(request.session)
            for items in cart.items:
                item = items.product
            order_obj = Orders(name = name, surname = surname,
                              phone = phone, email = email, item = item)
            order_obj.save()
            message = 'The dog was added to the cart'
            return HttpResponseRedirect(reverse('index'))
        else:
            form = OrderForm()
    return HttpResponseRedirect(reverse('index'))



def details(request, id):
    try:
        dog_details = Dogs.objects.get(id=id)
    except:
        raise Http404
    context = {
            'dog_details':dog_details
    }
    return render(request, 'djog/details.html', context)

