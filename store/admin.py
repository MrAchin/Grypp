from django.contrib import admin
from .models import Product  # Import your Product blueprint

# Register your model here so it shows up as a manageable section
admin.site.register(Product)