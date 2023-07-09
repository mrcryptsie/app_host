from django.shortcuts import render
from store.models import Product

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def paiement(request):
    return render(request, 'inscription.html')

def news(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products':products,
    }
    return render(request, 'news.html', context)

def read_more(request):
    return render(request, 'read_more.html')

def services(request):
    return render(request, 'services.html')
