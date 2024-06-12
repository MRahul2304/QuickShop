from django.shortcuts import render, redirect, HttpResponse
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import JsonResponse
import json

def csrf_failure(request, reason=""):
    return render(request, 'shop/csrf_failure.html', {"reason": reason})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        # handle login logic here
        pass
    return render(request, 'shop/login.html')

def home(request):
    products = Product.objects.filter(trending = 1)
    return render(request, "shop/home.html", {"products":products})

def favourite_view(request):
    if request.user.is_authenticated:
        favourite = Favourite.objects.filter(user=request.user)
        return render(request, "shop/favourite.html", {"favourite":favourite})
    else:
        return redirect("/")


def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, "shop/cart.html", {"cart":cart})
    else:
        return redirect("/")

def favourite(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['pid']
            product_status = Product.objects.get(id = product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status':'Product Already In Favourite'}, status = 200)
                else:
                    Favourite.objects.create(user=request.user, product_id=product_id)
                    return JsonResponse({'status':'Product Added To Favourite'}, status = 200)    
        else:
            return JsonResponse({'status':'Login to Add Favourite'}, status = 200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status = 200)
    
def remove_favourite_product(request, fid):
    item = Favourite.objects.get(id=fid)
    item.delete()
    return redirect("/favourite_view")

def add_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            #print(request.user.id)
            product_status = Product.objects.get(id = product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status':'Product Already In Cart'}, status = 200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status':'Product Added To Cart'}, status = 200)
                    else:
                        return JsonResponse({'status':'Out Of Stock'}, status = 200)
        else:
            return JsonResponse({'status':'Login to Add Cart'}, status = 200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status = 200)

def remove_cart_product(request, cid):
    cartitem = Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In")
                return redirect("/")
            else:
                messages.error(request, "Invalid User Name Or Password")
                return redirect("/login")
        return render(request, "shop/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out")
    return redirect("/")

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success")
            return redirect('/login')
    return render(request, "shop/register.html", {'form':form})
 
def collections(request):
    category = Category.objects.filter(status = 0)
    return render(request, "shop/collections.html", {"category":category})

def collectionsview(request, name):
    if(Category.objects.filter(name = name, status = 0)):
        products = Product.objects.filter(category__name = name)
        return render(request, "shop/products/index.html", {"products":products, "category_name": name})
    else: 
        messages.warning(request, "Category Not Found")
        return redirect('collections')
    
def product_details(request, cname, pname):
    if(Category.objects.filter(name = cname, status = 0)):
        if(Product.objects.filter(name = pname, status = 0)):
            products = Product.objects.filter(name=pname, status=0).first()
            return render(request, "shop/products/product_details.html", {"products":products})
        else:
            messages.error(request, "Product Not Found")
            return redirect('collections')
    
    else:
        messages.error(request, "Category Not Found")
        return redirect('collections')
