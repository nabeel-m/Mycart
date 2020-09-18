from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,"shop/about.html")

def fashion(request):
    return render(request,'shop/fashion.html')

def menfashion(request):
    return render(request,'shop/menfashion.html')

def shirts(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request,'shop/shirts.html',params)

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at requeest")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at productview")

def checkout(requeest):
    return HttpResponse("We are at checkout")