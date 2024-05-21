from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views 

urlpatterns = [
    # path('',views.home),
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name='product-detail'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('buy-now/',views.buy_now,name='buy-now'),
    path('address/',views.address,name='address'),
    path('orders/',views.orders,name='orders'),
    path('change-password/',views.change_password,name='change-password'),
    path('mobile/',views.mobile,name='mobile'),
    path('mobile/<slug:data>',views.mobile,name='mobiledata'),
    path('login/',views.login,name='login'),
    path('registration/',views.customerregistraion,name='registration'),
    path('checkout/',views.checkout,name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 