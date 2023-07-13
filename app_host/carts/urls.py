from django.urls import path
from . import views

urlpatterns = [
    path('', views.carts, name='carts'), 
    path('add_carts/<int:product_id>/', views.add_carts, name='add_carts'),

]