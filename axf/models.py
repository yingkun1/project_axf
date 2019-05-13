from django.db import models

# Create your models here.

class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1,self).get_queryset().filter(isDelete=False)

class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2,self).get_queryset().filter(isDelete=True)
