from django.shortcuts import redirect, render


from django.views import View
from django.views import generic 
from .models import Product,Customer,Cart,OrderPlaced
from .forms import CustomerProfileForm, CustomerRegistrationForm 

from django.views import View 
from .models import Product,Customer,Cart,OrderPlaced
from .form import CustomerProfileForm, CustomerRegistrationForm 

from django.views import View 
from .models import Product,Customer,Cart,OrderPlaced
from .form import CustomerProfileForm, CustomerRegistrationForm 

from django.contrib import messages 
from django.db.models import Q 
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        # print(topwears)
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request,'shop/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles,'laptop':laptop})
        


class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'shop/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})
        
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    #print(user,product_id)
    product= Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount 
                total_amount = amount + shipping_amount 
            
            return render(request,'shop/addtocart.html',{'carts':cart,'totalamount':total_amount,'amount':amount})
        else:
            return render(request,'shop/emptycart.html')
def plus_cart(request):
    if request.method == 'GET': 
        prod_id = request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1 
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount 
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount +shipping_amount,
        }
        # print(data)
        return JsonResponse(data)
def minus_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            
            
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount +shipping_amount 
        }
        return JsonResponse(data)

@login_required    
def remove_cart(request):
    if request.method =='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            
            
        data = {
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)
def buy_now(request):
    return render(request,'shop/buynow.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    
    return render(request,'shop/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request,'shop/orders.html',{'order_placed':op})

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

def login(request):
    return render(request,'shop/login.html')


# def logout(request):
#     return redirect('/accounts/login/')
class LogOut(generic.View):
    def get(self,request):
        LogOut()
        return redirect('/accounts/login/')

def logout(request):
    return redirect('/accounts/login/')


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
    
@login_required
def checkout(request):
    user=request.user
    add =Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount= 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.product.discounted_price * p.quantity)
            amount += tempamount
        totalamount = amount + shipping_amount 

    return render(request,'shop/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')


@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'shop/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user 
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations Profile Updated Successfully')
        return render(request,'shop/profile.html',{'form':form,'active':'btn-primary'})
    
