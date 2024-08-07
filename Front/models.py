from django.db import models
from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='meida/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Reja(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/',null=True, blank=True)
    money=models.IntegerField(default=10)
                             
    


class Category(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Coach(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    title=models.CharField(max_length=255)
    sports_name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='media/')
    is_active = models.BooleanField(default=True)



class Gym(models.Model):
    name = models.CharField(max_length=255)
    title=models.TextField()
    image=models.ImageField(upload_to='meida/')
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()

    def __str__(self):
        return self.name   
class Info (models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name
class Blog_name(models.Model):
    name = models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    age=models.IntegerField()
    image=models.ImageField(upload_to='blog_img/')
    def __str__(self):
        return self.name
                          
