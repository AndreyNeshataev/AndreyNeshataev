from decimal import Decimal
from django.conf import settings
from app_marketplace.models import Goods, Variation


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, variant, quantity=1, update_quantity=False):
        variant_id = str(variant.id)

        if variant_id not in self.cart:
            self.cart[variant_id] = {'quantity': 0,
                                     'price': str(variant.get_price()),
                                     'shop': variant.shop.name_shop,
                                     'amount': variant.quantity}
        if update_quantity:
            self.cart[variant_id]['quantity'] = quantity
        else:
            self.cart[variant_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        variant_ids = self.cart.keys()
        variants = Variation.objects.filter(id__in=variant_ids)
        for variant in variants:
            self.cart[str(variant.id)]['product'] = variant

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
