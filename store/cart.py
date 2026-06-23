# store/cart.py
from decimal import Decimal
from .models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize the session-based shopping cart locker.
        """
        self.session = request.session
        cart = self.session.get('session_cart')

        # If a fresh new visitor arrives, assign them an empty tracking bucket
        if not cart:
            cart = self.session[ 'session_cart' ] = {}
        self.cart = cart

    def add(self, product, quantity=1, size='M'):
        """
        Add a selected product variation securely into the session data drawer.
        """
        product_id = str(product.id)
        # Create a unique key tracking item combination + size selection
        item_key = f"{product_id}_{size}"

        if item_key not in self.cart:
            self.cart[ item_key ] = {
                'product_id': product_id,
                'price': str(product.price),
                'quantity': int(quantity),
                'size': size
            }
        else:
            self.cart[ item_key ][ 'quantity' ] += int(quantity)

        self.save()

    def __len__(self):
        """
        Count the cumulative number of apparel items currently in the cart.
        """
        return sum(item[ 'quantity' ] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculate total invoice valuation for checkout processes.
        """
        return sum(Decimal(item[ 'price' ]) * item[ 'quantity' ] for item in self.cart.values())

    def save(self):
        # Notify Django explicitly that the session data payload changed so it updates cookies
        self.session.modified = True