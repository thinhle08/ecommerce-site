from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    status = models.BooleanField(default=True, null=False)
    description = models.TextField(null=True)
    keyword = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.FloatField(null=False)
    size = models.TextField(null=True)
    image = models.FileField(upload_to='documents/')
    status = models.BooleanField(default=True, null=False)
    active_home = models.BooleanField(default=True, null=False)
    description = models.TextField(null=True)
    keyword = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Information_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='information',  null=True)
    image = models.FileField(upload_to='users/', default=None)
    phone = models.CharField(null=False, max_length=255, default=None)
    address = models.TextField(null=False, default='Không xác định ...')
    content = models.TextField(null=False, default='Không xác định ...')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pays = models.TextField(default='Thanh toán tiền mặt', max_length=255)
    address = models.TextField(null=False, default='Không xác định ...')
    phone = models.CharField(null=False, max_length=255, default=None)
    status = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(null=False)


class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pro = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)


class Wish_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pro = models.ForeignKey(Product, on_delete=models.CASCADE)



