from django.shortcuts import render
from . models.model_dogs import Dogs

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

def cart(request):
    return render(request, 'djog/cart.html')

def register(request):
    return render(request, 'djog/register.html')

def details(request, alias):
    dog_details = Dogs.objects.get(alias=alias)
    context = {
        'dog_details':dog_details
    }
    return render(request, 'djog/details.html', context)