from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('product-detail/',views.product_detail,name='product-detail'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart/'),
    path('buy-now/',views.buy_now,name='buy-now'),
    path('address/',views.address,name='address'),
]
