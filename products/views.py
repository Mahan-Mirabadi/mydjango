from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.db.models import Avg,Max,Min


# Create your views here.
def viewproduct(request):
    all_product = Product.objects.all()
    info=all_product.aggregate(Avg('price'),Max('price'),Min('price'),Max('ratings'))
    product_toll=Product.objects.all().count()
    return render(request, 'products/product_list.html', {'context': all_product, 'info':info,  'product_toll':product_toll})
def ViewProductDetails(request, s):
    product = get_object_or_404 (Product, slug=s)
    return render(request, 'products/product_details.html', {'product':product})
def ViewThanks(request):
    return render(request, 'products/thank_you_page.html')   
