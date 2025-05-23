from django.contrib import admin
from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'price', 'is_sold', 'manufacturer')
    list_filter = ('is_sold', 'manufacturer', 'body_type')
    search_fields = ('brand', 'model', 'vin')
    raw_id_fields = ('manufacturer', 'body_type', 'added_by')
    list_editable = ('price', 'is_sold')
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'car', 'status', 'total_amount')
    list_filter = ('status', 'manager')
    search_fields = ('customer__full_name', 'car__brand')
    date_hierarchy = 'order_date'
    ordering = ('-order_date',)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'warranty_years')
    search_fields = ('name', 'country')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'registration_date')
    search_fields = ('full_name', 'phone', 'passport')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'birth_date', 'gender')
    list_filter = ('position', 'gender')
    search_fields = ('full_name', 'passport')

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(BodyType)
admin.site.register(Position)
admin.site.register(Payment)