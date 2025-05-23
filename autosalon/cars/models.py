from django.db import models

class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True, db_column='manufacturer_id')
    name = models.CharField(max_length=100, db_column='name')
    country = models.CharField(max_length=200, db_column='country')
    warranty_years = models.IntegerField(default=2, db_column='warranty_years')

    class Meta:
        managed = False
        db_table = 'manufacturers'

    def __str__(self):
        return self.name

class BodyType(models.Model):
    body_type_id = models.AutoField(primary_key=True, db_column='body_type_id')
    name = models.CharField(max_length=30, unique=True, db_column='name')

    class Meta:
        managed = False  
        db_table = 'body_types'

    def __str__(self):
        return self.name

class Position(models.Model):
    position_id = models.AutoField(primary_key=True, db_column='position_id')
    position_name = models.CharField(max_length=100, db_column='position_name')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, db_column='salary')
    duties = models.TextField(blank=True, db_column='duties')
    requirements = models.TextField(blank=True, db_column='requirements')

    class Meta:
        managed = False  
        db_table = 'positions'

    def __str__(self):
        return self.position_name

class Staff(models.Model):
    GENDER_CHOICES = [('М', 'Мужской'), ('Ж', 'Женский')]
    
    staff_id = models.AutoField(primary_key=True, db_column='staff_id')
    full_name = models.CharField(max_length=100, db_column='full_name')
    birth_date = models.DateField(db_column='birth_date')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, db_column='gender')
    address = models.CharField(max_length=200, blank=True, db_column='address')
    phone = models.CharField(max_length=20, blank=True, db_column='phone')
    passport = models.CharField(max_length=20, db_column='passport')
    position = models.ForeignKey(
        Position, 
        on_delete=models.PROTECT, 
        db_column='position_id'
    )

    class Meta:
        managed = False  
        db_table = 'staff'

    def __str__(self):
        return self.full_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, db_column='customer_id')
    full_name = models.CharField(max_length=100, db_column='full_name')
    phone = models.CharField(max_length=20, db_column='phone')
    email = models.EmailField(blank=True, db_column='email')
    passport = models.CharField(max_length=20, db_column='passport')
    registration_date = models.DateField(auto_now_add=True, db_column='registration_date')

    class Meta:
        managed = False  
        db_table = 'customers'

    def __str__(self):
        return self.full_name

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('АКПП', 'Автоматическая'),
        ('МКПП', 'Механическая')
    ]
    
    car_id = models.AutoField(primary_key=True, db_column='car_id')
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.PROTECT, 
        db_column='manufacturer_id'
    )
    brand = models.CharField(max_length=50, db_column='brand')
    model = models.CharField(max_length=50, db_column='model')
    body_type = models.ForeignKey(
        BodyType,
        on_delete=models.PROTECT,
        db_column='body_type_id'
    )
    color = models.CharField(max_length=30, db_column='color')
    production_year = models.IntegerField(db_column='production_year')
    vin = models.CharField(max_length=17, unique=True, db_column='vin')
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1, db_column='engine_volume')
    power = models.IntegerField(db_column='power')
    transmission = models.CharField(
        max_length=4, 
        choices=TRANSMISSION_CHOICES,
        db_column='transmission'
    )
    price = models.DecimalField(max_digits=18, decimal_places=2, db_column='price')
    is_sold = models.BooleanField(default=False, db_column='is_sold')
    added_by = models.ForeignKey(
        Staff,
        on_delete=models.PROTECT,
        db_column='added_by'
    )
    add_date = models.DateTimeField(auto_now_add=True, db_column='add_date')

    class Meta:
        managed = False
        db_table = 'cars'

    def __str__(self):
        return f"{self.brand} {self.model}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Оформлен', 'Оформлен'),
        ('В процессе', 'В процессе'),
        ('Завершён', 'Завершён'),
        ('Отменён', 'Отменён')
    ]
    
    order_id = models.AutoField(primary_key=True, db_column='order_id')
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.PROTECT, 
        db_column='customer_id'
    )
    car = models.ForeignKey(
        Car, 
        on_delete=models.PROTECT, 
        db_column='car_id'
    )
    manager = models.ForeignKey(
        Staff, 
        on_delete=models.PROTECT, 
        db_column='manager_id'
    )
    order_date = models.DateTimeField(auto_now_add=True, db_column='order_date')
    sale_date = models.DateTimeField(null=True, blank=True, db_column='sale_date')
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='Оформлен',
        db_column='status'
    )
    total_amount = models.DecimalField(
        max_digits=18, 
        decimal_places=2, 
        default=0,
        db_column='total_amount'
    )
    prepayment_amount = models.DecimalField(
        max_digits=18, 
        decimal_places=2, 
        default=0,
        db_column='prepayment_amount'
    )

    class Meta:
        managed = False  
        db_table = 'orders'

    def __str__(self):
        return f"Заказ #{self.order_id}"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Наличные', 'Наличные'),
        ('Карта', 'Карта'),
        ('Кредит', 'Кредит'),
        ('Перевод', 'Перевод')
    ]
    
    payment_id = models.AutoField(primary_key=True, db_column='payment_id')
    order = models.ForeignKey(
        Order, 
        on_delete=models.PROTECT, 
        db_column='order_id'
    )
    amount = models.DecimalField(max_digits=18, decimal_places=2, db_column='amount')
    payment_date = models.DateTimeField(auto_now_add=True, db_column='payment_date')
    payment_method = models.CharField(
        max_length=20, 
        choices=PAYMENT_METHODS,
        db_column='payment_method'
    )

    class Meta:
        managed = False  
        db_table = 'payments'

    def __str__(self):
        return f"Платёж #{self.payment_id}"