# Create your views here.
# store/views.py
from django.http import HttpResponse

# store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .cart import Cart

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

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart_detail.html', {'cart': cart})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        size = request.POST.get('size', 'M')  # Fallback defaults to 'M' if none picked
        quantity = int(request.POST.get('quantity', 1))

        # Call your session cart engine's add function
        cart.add(product=product, quantity=quantity, size=size)

    return redirect('cart_detail')  # Redirect right to our new shopping bag page view