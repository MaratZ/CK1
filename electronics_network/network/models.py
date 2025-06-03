from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street} {self.house_number}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.model})"


class Supplier(models.Model):
    FACTORY = 0
    RETAIL = 1
    ENTREPRENEUR = 2

    LEVEL_CHOICES = [
        (FACTORY, 'Factory'),
        (RETAIL, 'Retail Network'),
        (ENTREPRENEUR, 'Individual Entrepreneur'),
    ]

    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=FACTORY)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_level_display()}: {self.name}"

    def save(self, *args, **kwargs):
        if not self.supplier:
            self.level = self.FACTORY
        elif self.supplier.level == self.FACTORY:
            self.level = self.RETAIL
        else:
            self.level = self.ENTREPRENEUR
        super().save(*args, **kwargs)


from django.db import models

# Create your models here.
