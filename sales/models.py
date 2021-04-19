from django.db import models
from products.models import Product
from customers.models import Customer
from users.models import Profile
from django.utils import timezone
from .utils import generate_code
# Create your models here.

class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    # para poder usar y editar el campo en el panel de admin
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == '':
            self.transaction_id = generate_code()

        if self.created_at is None:
            self.created_at = timezone.now()

        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def __str__(self):
        return f"Sales for the amount of ${self.total_price}"


class CSV(models.Model):
    file_name = models.FileField(upload_to='csv_files')
    # ya he usado este archivo?
    activated = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name