from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATAGORY = (
                ('Indoor', 'Indoor'),
                ('Out Door', 'Out Door')
                )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATAGORY)
    description= models.TextField(null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
             ('Pending','Pending'),
             ('Out for delevery', 'Out for delivery'),
             ('Delivered', 'Delivered')
             )
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS)