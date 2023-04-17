from django.db import models

# Create your models here.

    
class Items(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    is_invoice = models.BooleanField(default=False)

class Seller(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    items = models.ManyToManyField(Items)
    
class Buyer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    items = models.ManyToManyField(Items)
    
class Invoice(models.Model):
    buyer_id = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller,on_delete=models.CASCADE)
    items_ids = models.ManyToManyField(Items)
    creation_date = models.DateField(auto_now_add=True)
    
    
    
    