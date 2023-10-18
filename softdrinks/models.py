from django.db import models
from .validators import *
from django.core.validators import MaxValueValidator
from django.conf import settings

user = settings.AUTH_USER_MODEL

# Create your models here.
class soda(models.Model):
    Owner = models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    brand = models.CharField(max_length=100,null=False,validators=[validate_title])
    description = models.TextField(default="no description added here",validators=[validate_length])
    quantity = models.CharField(max_length=100,blank=True,validators=[validate_char])
    price = models.IntegerField(default=0,validators=[MaxValueValidator(1000,'value is above limit')])

    def __str__(self):
        return self.brand
