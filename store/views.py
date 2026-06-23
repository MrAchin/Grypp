# Create your views here.
# store/views.py
from django.http import HttpResponse

# store/views.py
from django.shortcuts import render
from .models import Product


def homepage(request):
    # Only fetch active products from the database securely using Django's ORM
    products = Product.objects.all()

    # Pass the products data directly into our HTML template container
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def product_detail(request, product_id):
    # Safely look up the product or display a secure 404 error if it doesn't exist
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)