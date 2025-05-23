from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rest_framework import viewsets
from .models import *
from .serializers import *

def car_list(request):
    # Базовый запрос - только непроданные авто
    cars = Car.objects.filter(is_sold=False)

     # Поиск по марке или модели (из параметра ?search=)
    search = request.GET.get('search')
    if search:
        cars = cars.filter(
            models.Q(brand__icontains=search) | 
            models.Q(model__icontains=search)
        )
    
    # Фильтр по минимальной цене (из параметра ?min_price=)
    min_price = request.GET.get('min_price')
    if min_price:
        try:
            cars = cars.filter(price__gte=float(min_price))
        except ValueError:
            pass  # Игнорируем нечисловые значения
    
    # Фильтр по максимальной цене (из параметра ?max_price=)
    max_price = request.GET.get('max_price')
    if max_price:
        try:
            cars = cars.filter(price__lte=float(max_price))
        except ValueError:
            pass
    
    # Фильтр по году выпуска (из параметра ?year=)
    year = request.GET.get('year')
    if year:
        try:
            cars = cars.filter(production_year=int(year))
        except ValueError:
            pass
    
    # Сортировка по цене (по умолчанию)
    cars = cars.order_by('price')
    
    # Пагинация
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cars/car_list.html', {
        'page_obj': page_obj,
        'filter_values': {
            'min_price': min_price,
            'max_price': max_price,
            'year': year
        }
    })


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all().order_by('name')
    return render(request, 'cars/manufacturer_list.html', {'manufacturers': manufacturers})

def order_list(request):
    orders = Order.objects.select_related('customer', 'car').order_by('-order_date')
    return render(request, 'cars/order_list.html', {'orders': orders})

def customer_list(request):
    customers = Customer.objects.all().order_by('full_name')
    return render(request, 'cars/customer_list.html', {'customers': customers})

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer