from django.db import models

from django.contrib.auth.models import User

class Contacto(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, null=True)
    phone3 = models.CharField(max_length=20, null=True)
    phone4 = models.CharField(max_length=20, null=True)
    phone5 = models.CharField(max_length=20, null=True)
    phone6 = models.CharField(max_length=20, null=True)
    phone7 = models.CharField(max_length=20, null=True)
    phone8 = models.CharField(max_length=20, null=True)
    phone9 = models.CharField(max_length=20, null=True)
    phone10 = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    email2 = models.EmailField(null=True)
    email3 = models.EmailField(null=True)
    email4 = models.EmailField(null=True)
    email5 = models.EmailField(null=True)
    email6 = models.EmailField(null=True)
    email7 = models.EmailField(null=True)
    email8 = models.EmailField(null=True)
    email9 = models.EmailField(null=True)
    email10 = models.EmailField(null=True)
    address = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, null=True)
    address3 = models.CharField(max_length=150, null=True)
    address4 = models.CharField(max_length=150, null=True)
    address5 = models.CharField(max_length=150, null=True)
    address6 = models.CharField(max_length=150, null=True)
    address7 = models.CharField(max_length=150, null=True)
    address8 = models.CharField(max_length=150, null=True)
    address9 = models.CharField(max_length=150, null=True)
    address10 = models.CharField(max_length=150, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.
