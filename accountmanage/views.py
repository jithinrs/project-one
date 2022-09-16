from django.shortcuts import render
from .forms import *
from .views import *
# Create your views here.


def useraccount(request):
    test = addressform()
    addr = useraddress.objects.filter(user_id = request.user).values()
    tests = {
        'addr' : addr
    }
    
    return render(request, 'useraccount/accounthome.html', tests)

def userorderhistory(request):
    return render(request, 'useraccount/userorder.html')