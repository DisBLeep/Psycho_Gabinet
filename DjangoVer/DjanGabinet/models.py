import datetime
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

# Create your models here.
atype = [
    ("A","Admin"), ("P","Pacjent"), ("L","Lekarz") ]

class Users2(models.Model):
    atype = models.CharField(max_length=200, choices=atype)
    first = models.CharField(max_length=50)
    last  = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addrs = models.CharField(max_length=50)
    postc = models.CharField(max_length=50)
    town  = models.CharField(max_length=50) 
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    def _str_(self):
        return self.first_name + ' ' + self.last_name