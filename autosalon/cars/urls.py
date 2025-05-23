from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# Для API
router = DefaultRouter()
router.register(r'api/cars', views.CarViewSet)
router.register(r'api/manufacturers', views.ManufacturerViewSet)
router.register(r'api/orders', views.OrderViewSet)
router.register(r'api/customers', views.CustomerViewSet)

urlpatterns = [
    # HTML-представления
    path('cars/', views.car_list, name='car-list'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('manufacturers/', views.manufacturer_list, name='manufacturer-list'),
    path('orders/', views.order_list, name='order-list'),
    path('customers/', views.customer_list, name='customer-list'),
    
    # Главная страница
    path('', views.car_list, name='home'),
] + router.urls  # Добавляем маршруты API