from django.shortcuts import redirect, render
from django.views import View 
from .models import Product,Customer,Cart,OrderPlaced
from .form import CustomerRegistrationForm 
from django.contrib import messages 
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
        

# def product_detail(request):
#     return render(request,'shop/productdetail.html')
class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'shop/productdetail.html',{'product':product})
        

def add_to_cart(request):
    return render(request,'shop/addtocart.html')

def buy_now(request):
    return render(request,'shop/buynow.html')
def address(request):
    return render(request,'shop/address.html')
def orders(request):
    return render(request,'shop/orders.html')
# def change_password(request):
#     return render(request,'shop/changepassword.html')
def mobile(request,data=None):
    if data == None:
        mobiles=Product.objects.filter(category='M')
    elif data=='Nokia' or data=='samsung':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=5000)
    elif data=='above':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=5000)

    return render(request,'shop/mobile.html',{'mobiles':mobiles})
def laptop(request,data=None):
    if data ==None:
        laptop=Product.objects.filter(category='L')
    elif data=='dell' or data=='Dell':
        laptop=Product.objects.filter(category='L').filter(brand=data)
    elif data=='above' :
        laptop = Product.objects.filter(category='L').filter(discounted_price__gt=50000)
    elif data=='below':
        laptop = Product.objects.filter(category="L").filter(discounted_price__lt=50000)
    return render(request,'shop/laptop.html',{'laptop':laptop})
def topwear(request,data=None):
    if data ==None:
        topwear = Product.objects.filter(category="TW")
    elif data == 'Lee':
        topwear = Product.objects.filter(category="TW").filter(brand=data)
    elif data == 'shorts':
        topwear = Product.objects.filter(category="TW").filter(brand=data)
    elif data == 'sporty':
        topwear = Product.objects.filter(category="TW").filter(brand=data)
    return render(request,'shop/topwear.html',{'topwear':topwear})
def bottomwear(request,data=None):
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data== 'above':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__gt=300)
    elif data == 'below':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=300)
    return render(request,'shop/bottomwear.html',{'bottomwear':bottomwear})
def profile(request):
    return render(request,'shop/profile.html')
def login(request):
    return render(request,'shop/login.html')
def logout(request):
    return redirect('/accounts/login/')
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm
        return render(request,'shop/customerregistration.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation Registered Successfully !!')
            form.save()
        return render(request,'shop/customerregistration.html',{'form':form})
# def customerregistraion(request):
#     return render(request,'shop/customerregistration.html')
def checkout(request):
    return render(request,'shop/checkout.html')
