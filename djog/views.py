from django.shortcuts import render

def index(request):
    return render(request, 'djog/index.html')

def login(request):
    return render(request, 'djog/login.html')

def logout(request):
    return render(request, 'djog/logout.html')

def cart(request):
    return render(request, 'djog/cart.html')

def register(request):
    return render(request, 'djog/register.html')

def details(request):
    """
    Just for preview
    """
    return render(request, 'djog/details.html')