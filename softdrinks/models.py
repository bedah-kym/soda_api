from django.db import models

# Create your models here.
class soda(models.Model):
    brand = models.CharField(max_length=100,null=False)
    description = models.TextField(default="no description added here")
    quantity = models.CharField(max_length=100,blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.brand
