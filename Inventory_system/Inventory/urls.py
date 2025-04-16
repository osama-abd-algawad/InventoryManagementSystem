from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Inventory'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),

    path('',views.product_list,name='product_list'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit/<int:product_id>/', views.manage_product, name='edit_product'),
    path('add/', views.manage_product, name='create_product'),

    path('category/',views.category_list,name='category_list'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('category/edit/<int:category_id>/', views.manage_category, name='edit_category'),
    path('category/add/', views.manage_category, name='create_category'),

    path('sales/', views.sales_list, name='sales_list'),
    path('sales/<int:pk>/', views.sales_detail, name='sales_detail'),
    path('sales/create/', views.create_sales, name='create_sales'),

    path('report/', views.inventory_report, name='inventory_report'),
]
