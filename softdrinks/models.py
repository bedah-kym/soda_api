from django.db import models

# Create your models here.
class soda(models.Model):
    brand = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.brand
