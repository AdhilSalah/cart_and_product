import json
from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductForm

def home(request):
    products = Products.objects.all()
    forms = ProductForm()
    context = {
        'product':products,
        'form':forms
    }

    return render(request,'index.html',context)

def add_product(request):

    if request.method =='POST':
        product_name = request.POST['product']
        image = request.FILES.get('image')
        price = request.POST['price']
        description = request.POST['description']
        Products.objects.create(product_name=product_name,image=image,price=price,description=description)

    return redirect(home)

def edit_data(request,pk):
    product = Products.objects.get(id=pk)
    
    if request.method=='POST':
        product_name = request.POST['product']
        image = request.FILES.get('image')
        price = request.POST['price']
        description = request.POST['description']

        if image is None:
            image = product.image
        product.product_name=product_name
        product.price=price
        product.image = image
        product.description = description
        product.save()

        return redirect(home)

    return redirect(home)

def delete_product(request,pk):

    product = Products.objects.get(id=pk)
    product.delete()


    return redirect(home)