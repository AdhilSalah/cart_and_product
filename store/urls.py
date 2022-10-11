from django.urls import path,include
from store import views

urlpatterns = [
path('',views.home,name='home'),
path('add_product',views.add_product,name='add_product'),
path('edit_data/<int:pk>',views.edit_data,name='edit_data'),
path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
]
