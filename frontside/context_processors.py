from products.models import *


def menulinks(request):
    links = Product.objects.all ()
    return dict(links = links)


def cartcount(request):
    
    try:
        rawcart = Cart.objects.filter(user = request.user)
        count = 0
        for item in rawcart:
            count = count + 1*int(item.product_qty)
        
        return dict(count = count)
    except:
        count = 0
        return dict(count = count)
