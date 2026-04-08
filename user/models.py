from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    dish_name = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.dish_name
class Customer(models.Model):
    name=models.CharField(max_length=255)
    phone=models.ImageField(max_length=10)
    table_no=models.IntegerField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)
    dish_name = models.CharField(max_length=500)
    price = models.IntegerField()
    Number_of_plate = models.IntegerField(null=True,blank=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.dish_name
# Create your models here.
#class Manager(models.Model):
#    name=models.CharField(max_length=255,default="")
#    mobile=models.CharField(max_length=11)
#    password=models.CharField(max_length=255)
#    c_password=models.CharField(max_length=255,default="")
#        
#    def __str__(self):
#        return self.name