from django.shortcuts import render,redirect
from .models import Categories, Product, SubCategory
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.http import HttpResponse

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
    template_name = 'categorylist.html'


class Categoryadd(adminrequiredmixin, SuccessMessageMixin, CreateView):
    model = Categories
    success_message = 'Category Added'
    fields = "__all__"
    template_name = "categoryadd.html"
    

class Categoryupdate(adminrequiredmixin ,SuccessMessageMixin, UpdateView):
    model = Categories
    success_message = 'Category Updated'
    fields = "__all__"
    template_name = "categoryupdate.html"

class SubCategorylist(adminrequiredmixin,ListView):
    model = SubCategory
    template_name = 'subcategorylist.html'

    def get_queryset(self):
        # test1 = SubCategory.objects.filter(category_id = slug).values()
        return super().get_queryset().filter(category_id=self.kwargs['id'])


class SubCategoryadd(adminrequiredmixin ,SuccessMessageMixin, CreateView):
    model = SubCategory
    success_message = 'Category Added'
    fields = "__all__"
    template_name = "subcategoryadd.html"

class SubCategoryupdate(SuccessMessageMixin, UpdateView):
    model = SubCategory
    success_message = 'Sub Category Updated'
    fields = "__all__"
    template_name = "subcategoryupdate.html"


class Productlist(adminrequiredmixin, ListView):
    model = Product
    template_name = 'productlist.html'

class Productadd(adminrequiredmixin, SuccessMessageMixin, CreateView):
    model = Product
    success_message = 'Product Added'
    fields = "__all__"
    template_name = "productadd.html"

class Productupdate(SuccessMessageMixin, UpdateView):
    model = Product
    success_message = 'Product Updated'
    fields = "__all__"
    template_name = "productUpdate.html"

def category_delete(request, id):
    if request.method == 'POST':
        category_id = Categories.objects.get(pk=id)
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
    return render(request, 'adminbase.html')