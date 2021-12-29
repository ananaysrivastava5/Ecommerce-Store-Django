from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .basket import Basket
from store.models import Product


# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    context = {
        'basket': basket
    }
    return render(request, 'store/basket/summary.html', context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({ 'qty': basket_qty })
        return response 
    
    