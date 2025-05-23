"""
URL configuration for autosalon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Автомобили
    path('cars/', views.car_list, name='car-list'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    
    # Производители
    path('manufacturers/', views.manufacturer_list, name='manufacturer-list'),
    
    # Заказы
    path('orders/', views.order_list, name='order-list'),
    
    # Клиенты
    path('customers/', views.customer_list, name='customer-list'),
    
    # Главная страница
    path('', views.car_list, name='home'),
]
