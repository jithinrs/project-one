from datetime import date, datetime, timedelta
from django.shortcuts import render,redirect

from django.db.models import Sum
from authentications.models import Account
from .models import Categories, Product, Specification, SubCategory
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.http import HttpResponse
from django.contrib import messages
from .form import *
from accountmanage.models import Order, OrderItem
from accountmanage.forms import newstatus
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.
#custom decorator

class adminrequiredmixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return render(request, '404error.html')
        if not request.user.is_admin:
            return render(request, '404error.html')
        return super(adminrequiredmixin, self).dispatch(request, *args, **kwargs)

class Categorylist(adminrequiredmixin, ListView):
    model = Categories
    template_name = 'adminside/categorylist.html'


class Categoryadd(adminrequiredmixin, SuccessMessageMixin, CreateView):
    model = Categories
    success_message = 'Category Added'
    fields = "__all__"
    template_name = "adminside/categoryadd.html"


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['Subcategory'].queryset = SubCategory.objects.none()

    # def post(self, request, *args, **kwargs):
    #     self.title = self.title.title()
    #     return super(Categoryadd, self).post(request, *args, **kwargs)

    # def form_valid(self, form):
    #     form.instance.title = self.title.title()
    #     return super(Categoryadd, self).form_valid(form)
    

class Categoryupdate(adminrequiredmixin ,SuccessMessageMixin, UpdateView):
    model = Categories
    success_message = 'Category Updated'
    fields = "__all__"
    template_name = "adminside/categoryupdate.html"

class SubCategorylist(adminrequiredmixin,ListView):
    model = SubCategory
    template_name = 'adminside/subcategorylist.html'

    def get_queryset(self):
        # test1 = SubCategory.objects.filter(category_id = slug).values()
        return super().get_queryset().filter(category_id=self.kwargs['id'])

class SubCategoryFullList(adminrequiredmixin,ListView):
    model = SubCategory
    template_name = 'adminside/subcategoryfulllist.html'

class SubCategoryadd(adminrequiredmixin ,SuccessMessageMixin, CreateView):
    model = SubCategory
    success_message = 'Category Added'
    fields = "__all__"
    template_name = "adminside/subcategoryadd.html"

class SubCategoryupdate(SuccessMessageMixin, UpdateView):
    model = SubCategory
    success_message = 'Sub Category Updated'
    fields = "__all__"
    template_name = "adminside/subcategoryupdate.html"


class Productlist(adminrequiredmixin, ListView):
    model = Product
    template_name = 'adminside/productlist.html'

class Productadd(adminrequiredmixin, SuccessMessageMixin, CreateView, ProductsAddforms):
    model = Product
    success_message = 'Product Added'
    fields = "__all__"
    template_name = "adminside/productadd.html"


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['subcategories_id'].queryset = SubCategory.objects.none()

class Productupdate(SuccessMessageMixin, UpdateView):
    model = Product
    success_message = 'Product Updated'
    fields = "__all__"
    template_name = "adminside/productUpdate.html"

class Productspec(SuccessMessageMixin,CreateView):
    model = Specification
    success_message: str = "Specification added"
    fields = "__all__"
    template_name = "adminside/productspec.html"

def SingleProduct(request,cat_slug, subcat_slug, pro_slug):
    product = Product.objects.filter(url_slug = pro_slug, subcategories_id__url_slug = subcat_slug)
    tests = {
        'product' : product
    }
    return render(request, 'adminside/productpage.html', tests)

def category_delete(request, id):
    if request.method == 'POST':
        category_id = Categories.objects.get(pk=id)
        name = Categories.objects.filter(id=id).values('title')
        print(name)
        messages.success(request, f" {name[0]['title']} category is deleted")
        category_id.delete()
        return redirect('categorylist')

def subcategory_delete(request, id):
    if request.method == 'POST':
        subcategory_id = SubCategory.objects.get(pk=id)
        subcategory_id.delete()
        return redirect('categorylist')

def product_delete(request, id):
    if request.method == 'POST':
        product_id = Product.objects.get(pk=id)
       
        product_id.delete()
        return redirect('productlist')

def adminbase(request):
    order = Order.objects.all().filter().order_by('-created_at')[:10]

    mostpopular = Product.objects.annotate(test = Count('productcount')).order_by('-test')[:4]
    count = []
    name = []
    for mo in mostpopular:
        x = mo.test
        count.append(x)
        y = mo.product_name
        name.append(y)

    count1 = count[0]
    count2 = count[1]
    count3 = count[2]
    count4 = count[3]

    name1 = name[0]
    name2 = name[1]
    name3 = name[2]
    name4 = name[3]


    print(count,name)
    cod = Order.objects.filter(payment_mode = "COD").count()
    razor = Order.objects.filter(payment_mode = "Paid by Razerpay").count()
    paypal = Order.objects.filter(payment_mode = "Paid by PayPal").count()
    print(cod)

    today = date.today()

    day = today.day
    month = today.month
    year = today.year

    print(day)
    total_products = Product.objects.all().count()
    total_users = Account.objects.all().count()

    order_in_a_day = Order.objects.filter(created_at__year=year, created_at__month=month, created_at__day=day).count()
    print(order_in_a_day)
    # diff = datetime.today() - timedelta(days=2)
    # diff2 = datetime.today() - timedelta(days=3)
    # diff3 = datetime.today() - timedelta(days=4)
    # diff4 = datetime.today() - timedelta(days=5)
    # diff5 = datetime.today() - timedelta(days=6)
    # diff6 = datetime.today() - timedelta(days=7)
    # diff7 = datetime.today() - timedelta(days=10)

    # april = Order.objects.filter(created_at__gte = diff).count()
    # may = Order.objects.filter(created_at__gte = diff2).count()
    # june = Order.objects.filter(created_at__gte = diff3).count()
    # july = Order.objects.filter(created_at__gte = diff5).count()
    # august = Order.objects.filter(created_at__gte = diff6).count()
    # september = Order.objects.filter(created_at__gte = diff7).count()



    
    revenue = Order.objects.all().aggregate(Sum('total_price'))
    total_revenue = revenue['total_price__sum']
    total_orders = Order.objects.all().count()


    context = {
        "order" : order,
        "cod" : cod,
        "razor" : razor,
        "paypal" : paypal,
        # "july" : july,
        # "august" : august,
        # "september" : september,
        # "june" : june,
        # "may" : may,
        # "april" : april,
        "total_revenue" : total_revenue,
        "total_orders" : total_orders,
        "order_in_a_day" : order_in_a_day, 
        "total_users" : total_users,
        "total_products" : total_products,
        "name1" : name1,
        "name2" : name2,
        "name3" : name3,
        "name4" : name4,
        "count1" : count1,
        "count2" : count2,
        "count3" : count3,
        "count4" : count4,
    }
    return render(request, 'adminside/adminhome.html', context)

def adminorder(request):
    order = Order.objects.all().filter().order_by('-created_at')

    p = Paginator(Order.objects.all().filter().order_by('-created_at'), 5)
    page = request.GET.get('page')
    orders = p.get_page(page)

    form = newstatus()
    context = {
        'order' : order,
        'form' : form,
        'orders' : orders
    }
    return render(request, 'adminside/orderlist.html', context)

def update_admin_order(request,id):
    if request.method == 'POST':
        instance = get_object_or_404(Order, id=id)
        status = request.POST.get('status')
        instance.status = status
        instance.save()
        return redirect('orderlist')



def sales_report(request):
    today = datetime.today()
    year = datetime.now().year

    month = today.month

    orders = Order.objects.filter(created_at__month=month).values('oderuser__product_id__product_name','oderuser__product_id__in_stock_total',
    total = Sum('total_price'),).annotate(dcount=Sum('oderuser__quantity')).order_by()
    total_payment_amount = Order.objects.filter(created_at__month=month).aggregate(Sum('total_price'))


    ordersy = Order.objects.filter(created_at__year=year).values('oderuser__product_id__product_name','oderuser__product_id__in_stock_total',
    total = Sum('total_price'),).annotate(dcount=Sum('oderuser__quantity')).order_by()
    total_payment_amounty = Order.objects.filter(created_at__year=year).aggregate(Sum('total_price'))

    print(total_payment_amount)
    print(orders)
    context = {
        'orders':orders,
        'total_payment_amount':total_payment_amount,
        'ordersy' : ordersy,
        'total_payment_amounty' : total_payment_amounty
    }
    return render(request,'adminside/sales-report.html',context)  




def adminProView(request,cat_slug, subcat_slug, pro_slug):
    product = Product.objects.filter(url_slug = pro_slug, subcategories_id__url_slug = subcat_slug)
    tests = {
        'product' : product
    }
    return render(request, 'adminside/adminproduct.html', tests)