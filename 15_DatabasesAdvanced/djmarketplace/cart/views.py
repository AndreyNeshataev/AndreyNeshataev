from django.shortcuts import render, redirect, get_object_or_404
from app_marketplace.models import Variation
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app_users.models import PurchaseHistory
from django.utils.translation import gettext_lazy as _


@login_required(login_url="/users/login")
def cart_add(request, variant_id):
    cart = Cart(request)
    variant = get_object_or_404(Variation, id=variant_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(variant=variant,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        cart.add(variant=variant)
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Variation, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_payment(request):
    cart = Cart(request)
    total = cart.get_total_price()
    user = request.user
    if total <= user.profile.balance:
        user.profile.balance = float(user.profile.balance) - float(total)
        user.profile.save()
        for item in cart:
            var = Variation.objects.get(id=item['product'].id)
            PurchaseHistory.objects.create(user=user,
                                           goods=var.product,
                                           quantity=item['quantity'],
                                           price=item['price'],
                                           total_price=item['total_price'],
                                           shop=var.shop)
            if var.quantity >= int(item['quantity']):
                var.quantity -= int(item['quantity'])
                var.save()
            else:
                return HttpResponse(_(f"Количество товара к покупке в магазине"
                                      f"{var.shop} больше чем имеется на складе магазина"))
    else:
        return HttpResponse(_("Недостаточно средств, пополните баланс, или уберите один из выбранных товаров"))
    cart.clear()
    return redirect('home')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
