from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from customer.models import Customer
from order.models import Order
from product.models import Product


def cart(request):
    if request.session.get('cart'):
        the_cart = request.session.get('cart')
        total = 0
        product_list = dict()

        for i in the_cart:
            product = Product.objects.filter(id=i).first()
            product_list[product] = the_cart[i]
            total += product.initial_price * int(the_cart[i])

        context = {
            'products': product_list,
            'total': total,
        }
        return render(request, 'order/cart.html', context)

    return render(request, 'order/cart.html', {'request': request})


@csrf_exempt
def single_product(request):
    if request.method == 'POST':
        product_id = request.POST['id']
        selected_product = get_object_or_404(Product, id=product_id)
        return render(request, 'product/single_product.html', {'request': request, 'product': selected_product})
    return render(request, 'product/single_product.html', {'request': request})


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        qty = request.POST['qty']
        if not request.session.get('cart'):
            request.session['cart'] = {
                product_id: qty
            }
        else:
            the_cart = request.session.get('cart')
            the_cart[product_id] = qty
            request.session.modified = True

        print(request.session.get('cart'))
        return redirect("order:cart")


def delete_from_cart(request, product_id):
    the_cart = request.session.get('cart')
    the_cart.pop(str(product_id))
    request.session.modified = True
    return redirect("order:cart")


def checkout(request):
    if request.user.is_authenticated:
        # .
        # .
        # .
        # order = Order.objects.create(user=request.user,
        #                              address=Customer.address,
        #                              total_price=total_price,
        #                              )
        messages.success(request, 'Your order Recorded successfully')
        return render(request, "order/checkout_done.html", {'request': request})
    else:
        return render(request, "customer/login.html", {'request': request})
