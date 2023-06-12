from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = RichTextField()
    price = models.IntegerField(blank=False, null=False)
    cover = models.FileField(upload_to='files/product_covers/')
    promote = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=128)


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


class ProductFile(models.Model):
    file = models.FileField(upload_to='files/product_files/', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='files')


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=True, blank=True)

    def __str__(self):
        return self.user.username
