from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def categories(request):    # this view will available on every page. 
    return {                #Check settings.py->template->options->store.views.categories
        'categories': Category.objects.all()
    }
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {
        'product': product
    }
    return render(request, 'store/products/detail.html', context)