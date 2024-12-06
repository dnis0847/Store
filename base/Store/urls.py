from django.urls import path
from . import views

app_name = 'Store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'), # product_detail(product_id)
    path('add_product/', views.add_product, name='add_product'),
    path('search/', views.product_search_view, name='product_search_view'),
]