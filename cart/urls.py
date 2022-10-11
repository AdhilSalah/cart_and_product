from unicodedata import name
from django.urls import path,include
from cart import views

urlpatterns = [
path('cart_home',views.cart_home,name='cart_home'),
path('add_cart/<int:pk>/',views.add_cart,name='add_cart'),
path('viewcart/',views.view_cart,name='viewcart'),
path('delete_cart/<int:pk>/',views.delete_cart,name='delete_cart'),

]
