from decimal import Decimal
from myapp.models import Product
CART_ID = "cart"


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_ID)
        if not cart:
            cart = self.session[CART_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
        else:

            self.cart[product_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True

    def list(self):
        carts = []
        for product_id in self.cart.keys():
            obj = Product.objects.get(id=product_id)
            tmp_cart = {
                'id': product_id,
                'obj': obj,
                'quantity': self.cart[product_id]['quantity'],
                'price': Decimal(int(self.cart[product_id]['quantity']) * float(obj.price))
            }
            carts.append(tmp_cart)
        return carts

    def get_total_items(self):
        return sum(int(v['quantity']) for v in self.cart.values())

    def update(self, quantity, product_id):
        pid = str(product_id)
        self.cart[pid]['quantity'] = quantity
        self.save()
        print(self.cart)

    def delete(self, product_id):
        pid = str(product_id)
        del self.cart[pid]
        self.save()

