from rest_framework import serializers
from .models import soda

class sodaserializer (serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='soda-detail',lookup_field="pk")
    class Meta:
        model = soda
        fields = [
            'url',
            'pk',
            'brand',
            'description',
            'quantity',
            'price'
            ]
 