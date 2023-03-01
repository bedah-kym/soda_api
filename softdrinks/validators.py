from rest_framework import serializers


def validate_title(value):
    from .models import soda
    qs = soda.objects.filter(brand__iexact=value)
    if qs.exists():
       raise serializers.ValidationError(f"{value} ,is already a product name")

    return value
# stuff below could be done by importing validators in the models but i needed to learn this method
def validate_length(value):
    length = len(value)
    if length > 200 :
        raise serializers.ValidationError("description too long")
    return value

def validate_char(value):
    length = len(value)
    if length > 20:
        raise serializers.ValidationError("use short quantity abbreviations eg 50ml")
    return value

