from http.client import HTTPResponse
from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
from shop.form import CustomUserForm

# Create your views here.
def home(request):
    products = Product.objects.filter(trending=1)
    context = {
        "products" : products
   }
    return render(request, "shop/index.html", context)

def login(request):
    return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now..!")
            return redirect('/Login')
    context = {
        'form' : form
    }
    return render(request, "shop/register.html",context)

def collections(request):
    category = Category.objects.filter(status = 0)
    return render(request, "shop/collections.html", {"category":category})

def collectionsview(request,name):
    if(Category.objects.filter(name = name, status = 0)):
        products = Product.objects.filter(category__name = name)
        return render(request, "shop/products/index.html", {"products":products, "category_name":name})
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname, status=0)):
        if(Product.objects.filter(name=pname, status=0)):
            products = Product.objects.filter(name=pname, status=0).first()
            return render(request, "shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collections')
    else:
        messages.error(request,"No such Category Found")
        return redirect('collections')

    
