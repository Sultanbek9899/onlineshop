from django.urls import path
from . import views

urlpatterns=[
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug:category_slug>/', views.ProductListView, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]