from django.shortcuts import render,redirect
from cart.models import Cart

from store.models import Products

def cart_home(request):
    product = Products.objects.all()
    context = {
        'product':product
    }

    return render(request,'cart.html',context)

def add_cart(request,pk):

    if Cart.objects.filter(product_id=pk).exists():

        cart =  Cart.objects.get(product_id=pk)
        cart.quantity+=1
        cart.save()
    else:
        Cart.objects.create(product_id=pk,quantity=1)
    

    return redirect(view_cart)

def view_cart(request):
    total = 0
    amonunt=0
    cart = Cart.objects.all()

    for item in cart:
        amonunt=item.quantity*item.product.price
        total +=amonunt
        
        
    context = {
        'cart':cart,
        'total':total
    }
    return render(request,'viewcart.html',context)

def delete_cart(request,pk):
    try:
        cart = Cart.objects.get(product_id=pk)
        if cart.quantity <=1:
            cart.delete()
        else:
            cart.quantity-=1
            cart.save()
    except :
        pass
    return redirect(view_cart)


