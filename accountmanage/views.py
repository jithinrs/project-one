from django.shortcuts import render, redirect

from accountmanage.models import Order,OrderItem
from .forms import *
from .views import *
from django.contrib import messages

from django.views.generic import CreateView, ListView, UpdateView


# Create your views here.


def useraccount(request):
    test = addressform()
    addr = useraddress.objects.filter(user_id = request.user)
    tests = {
        'addr' : addr
    }
    
    return render(request, 'useraccount/accounthome.html', tests)

def addaddress(request):
    if request.method == "POST":
        form = addressform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "update succesful")
            return  redirect('useraccount')
        else:
            print(form.errors.as_data())
            messages.error(request,"you are a FAILURE!!")
    data = useraddress.objects.filter(user_id = request.user)
    context = {
        'data' : data
    }
    return render(request, 'useraccount/useraddaddress.html', context)

def updateaddress(request,id):
    addr = useraddress.objects.get(id=id)
    form = addressform(instance = addr)
    print(form)
    if request.method == 'POST':     
        form = addressform(request.POSt, instance = addr)
        if form.is_valid():
            form.save()
            return redirect('useraccount')
        else:
            print(form.errors.as_data())
    return render(request,'useraccount/userupdateaddress.html', {'form' : form})


# def userorderhistory(request):
#     ord = Order.objects.filter(user_id = request.user)
#     test = []
#     for obj in ord:

#         pro = OrderItem.objects.filter(order_id = obj.id)
#         test.append(pro)

#     print(test[1][0].price)
#     context = {
#         'test' : test
#     }
#     return render(request, 'useraccount/userorder.html', context)



class useroderhistory(ListView):
    model = Order
    template_name = 'useraccount/userorder.html'