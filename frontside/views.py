from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from products.models import SubCategory, Categories, Product

# Create your views here.

def home(request):
    return render(request, 'userside/landingpage.html')

def shop(request):
    category = Categories.objects.all()
    productss = Product.objects.all()
    test = {
        'category':category,
        'productss':productss
        }
    return render(request, 'userside/shop.html', test)



# class SingleProView(DetailView):
#     model = Product
#     template_name = 'userside/productview.html'


def SingleProView(request, url_slug):
    product = Product.objects.filter(url_slug = url_slug)
    tests = {
        'product' : product
    }
    return render(request, 'userside/productpage.html', tests)

def cart(request):
    return render(request,'userside/cart.html')