
from itertools import product
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from accountmanage.models import Order, OrderItem
from products.models import SubCategory, Categories, Product, Cart, discount,wishlist
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from accountmanage.models import useraddress
from accountmanage.forms import addressform
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
# Create your views here.

def home(request):
    return render(request, 'userside/landingpage.html')

@never_cache
def shop(request):
    category = Categories.objects.all()
    productss = Product.objects.all()
    test = {
        'category':category,
        'productss':productss
        }
    return render(request, 'userside/shop.html', test)


def shopcat(request,id):
    category = Categories.objects.all()
    productss = Product.objects.filter(subcategories_id__id__contains = id)
    test = {
        'category' : category,
        'productss': productss
    }
    return render(request, 'userside/catshop.html', test)



# class SingleProView(DetailView):
#     model = Product
#     template_name = 'userside/productview.html'


def SingleProView(request,cat_slug, subcat_slug, pro_slug):
    product = Product.objects.filter(url_slug = pro_slug, subcategories_id__url_slug = subcat_slug)
    tests = {
        'product' : product
    }
    return render(request, 'userside/productpage.html', tests)

def AddToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=product_id)
            if(product_check):
                if(Cart.objects.filter(user = request.user.id, product = product_id)):
                    return JsonResponse({"Status" : "Product already in cart"})

                else:
                    prod_qty = int(request.POST.get('product_qty'))
            
                    if product_check.in_stock_total >= prod_qty : 
                        Cart.objects.create(user = request.user, product = product_check, product_qty = prod_qty)
                        return JsonResponse({"Status" : "product added succesfully"})
                    
                    else : 
                        return JsonResponse({"Status" : "Only" +  str(product_check.in_stock_total) + " quantity available"})

            else:
                return JsonResponse({"Status" : "No product exist"})


                
            
        else:
            return JsonResponse({"Status" : "Login to continue"})


    return redirect('/')

def calcprice(qty, price):
    return int(qty) * int(price)


def cart(request):
    cart = Cart.objects.filter(user=request.user).order_by('created_at')
    context = {'cart' : cart}
    return render(request,'userside/carttest.html', context)

def updateCart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user = request.user, product_id = prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id =  prod_id, user = request.user)
            cart.product_qty = prod_qty
            cart.save()
            qty_now = cart.product_qty
            price = Product.objects.get(id = prod_id)
            print(price)
            pricec = price.product_max_price
            npricere = calcprice(qty_now, pricec)
            try:
                disc = discount.objects.get(product_id = prod_id)
                discp = disc.disc_percent
                dpricere = calcprice(qty_now, discp)
            except:
                dpricere = npricere
            print(dpricere)
            return JsonResponse({
                "Status" : "Updated Succesfully",
                'npricere' : npricere,
                'dpricere' : dpricere
                })
    return redirect('/')



def deleteCartItem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user = request.user, product_id = prod_id)):
            cartitem = Cart.objects.get(product_id = prod_id, user = request.user)
            cartitem.delete()
        return JsonResponse({"Status" : "Deleted Succesfully"})
    return redirect('/')


def checkout(request):
    addr = useraddress.objects.filter(user_id = request.user)

    rawcart = Cart.objects.filter(user = request.user)
    for item in rawcart:
        if item.product_qty > item.product.in_stock_total:
            Cart.objects.delete(id = item.id)
    
    cartitems = Cart.objects.filter(user = request.user)
    total_price = 0
    disc_prices = 0
    for item in cartitems:
        try:
            disc_pr = discount.objects.get(product_id = item.product_id)
            disc_prices = disc_prices + int(item.product_qty) * int(item.product.product_max_price) * (1 - int(disc_pr.disc_percent)/100)
        except:
            disc_prices = disc_prices + int(item.product_qty) * int(item.product.product_max_price)
        total_price = total_price + int(item.product.product_max_price) * int(item.product_qty)
    discount_red = total_price - disc_prices
    print(discount_red)
    context = {
        'cartitems' : cartitems, 
        'total_price' : total_price,
        'disc_prices' : disc_prices,
        'discount_red' : discount_red,
        'addr' : addr,
    }
    return render(request,'userside/checkout.html', context )

@login_required
def placeorder(request):
    
    if request.method == 'POST':
        form = addressform(request.POST)
        if form.is_valid():
            neworder = Order()
            neworder.user_id = request.user
            neworder.name = request.POST.get('name')
            neworder.email = request.POST.get('email')
            neworder.mobile = request.POST.get('mobile')
            neworder.address_1 = request.POST.get('address_1')
            neworder.address_2 = request.POST.get('address_2')
            neworder.city = request.POST.get('city')
            neworder.district = request.POST.get('district')
            neworder.state = request.POST.get('state')
            neworder.pincode = request.POST.get('pincode')

            neworder.payment_mode = request.POST.get('payment_mode')


            cartitems = Cart.objects.filter(user = request.user)
            total_price = 0
            disc_prices = 0
            for item in cartitems:
                try:
                    disc_pr = discount.objects.get(product_id = item.product_id)
                    disc_prices = disc_prices + int(item.product_qty) * int(item.product.product_max_price) * (1 - int(disc_pr.disc_percent)/100)
                except:
                    disc_prices = disc_prices + int(item.product_qty) * int(item.product.product_max_price)
                    total_price = total_price + int(item.product.product_max_price) * int(item.product_qty)
            neworder.total_price = disc_prices
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            tracking_no = current_date + str(neworder.user_id)
            neworder.tracking_no = tracking_no
            neworder.save()
            
            neworderitems = Cart.objects.filter(user = request.user)
            for item in neworderitems:
                OrderItem.objects.create(
                    order_id =  neworder,
                    product_id = item.product,
                    price = item.product.product_max_price,
                    quantity = item.product_qty
                )

                orderproduct = Product.objects.filter(id=item.product_id).first()
                orderproduct.in_stock_total = orderproduct.in_stock_total - item.product_qty
                orderproduct.save()


            Cart.objects.filter(user = request.user).delete()
            messages.success(request,'test work')

            return redirect('/')
        else:
            print(form.errors.as_data())
    messages.success(request,'test didnot  works')
    return redirect('shop')


def testsubmit(request):
    if request.method == 'POST':
        return redirect('shop')



def wish_list(request):
    pass

