from rest_framework import serializers
from .models import soda

class sodaserializer (serializers.ModelSerializer):
    class Meta:
        model = soda
        fields = ['brand','description','quantity','price']
 