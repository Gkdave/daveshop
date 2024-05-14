from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('product-detail/',views.product_detail,name='product-detail'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart/'),
    path('buy-now/',views.buy_now,name='buy-now'),
    path('address/',views.address,name='address'),
    path('orders/',views.orders,name='orders'),
    path('change-password/',views.change_password,name='change-password'),
    path('mobile/',views.mobile,name='mobile'),
    path('login/',views.login,name='login'),
    path('registration/',views.customerregistraion,name='registration'),
    path('checkout/',views.checkout,name='checkout'),
]
