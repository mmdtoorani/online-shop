from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from product.models import Product


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['id']
        selected_product = get_object_or_404(Product, id=product_id)
        return render(request, 'customer/cart.html', {'request': request, 'product': selected_product})
    if request.method == 'GET':
        print(request.session.get('product_name'))
        # request.session
        return HttpResponse("out of if block")


def cart(request):
    pass
