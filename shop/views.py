from django.shortcuts import render
from django.views import View 
from .models import Product

# def home(request):
#     hello = "This is dave's shop "
#     return render(request,'shop/home.html',{'hello':hello})
class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        # print(topwears)
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request,'shop/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles,'laptop':laptop})
        

def product_detail(request):
    return render(request,'shop/productdetail.html')

def add_to_cart(request):
    return render(request,'shop/addtocart.html')

def buy_now(request):
    return render(request,'shop/buynow.html')
def address(request):
    return render(request,'shop/address.html')
def orders(request):
    return render(request,'shop/orders.html')
def change_password(request):
    return render(request,'shop/changepassword.html')
def mobile(request):
    return render(request,'shop/mobile.html')
def login(request):
    return render(request,'shop/login.html')
def customerregistraion(request):
    return render(request,'shop/customerregistration.html')
def checkout(request):
    return render(request,'shop/checkout.html')
