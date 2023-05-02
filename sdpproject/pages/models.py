from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe



# Create your models here.
#
# class Customer(models.Model):
#     user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name=models.CharField(max_length=200, null=True)
#     email=models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     name=models.CharField(max_length=200)
#     price=models.BooleanField(default=False, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class ContactPage(models.Model):
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mail=models.CharField(max_length=20)
    country=models.CharField(max_length=10)
    para=models.CharField(max_length=200)

    def __str__(self):
        return self.username



class SellPage(models.Model):
    cname=models.CharField(max_length=30)
    pname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=6)
    ptype=models.CharField(max_length=30,default='Mens ware')
    price=models.CharField(max_length=30)
    prange=models.CharField(max_length=30,default='₹100-₹500')
    comment=models.CharField(max_length=30)

    def __str__(self):
        return self.cname


class Wcstore(models.Model):
    name=models.CharField(max_length=50)
    price = models.FloatField()
    #image=models.ImageField(upload_to='photos')

    def short_description(self):
        return truncatechars(self.description, 20)

    #def admin_photo(self):
        #return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
    #admin_photo.short_description='Image'
    #admin_photo.allow_tags=True

    def __str__(self):
        return self.name