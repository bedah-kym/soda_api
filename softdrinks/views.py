from .serializers import sodaserializer
from rest_framework import generics
from .models import soda
from .permissions import IsStaffEditorPermissions
from . import mixins

class DrinksList(mixins.UserQuerySetMixin,generics.ListCreateAPIView):
    queryset = soda.objects.all()
    serializer_class = sodaserializer
    permission_classes =[IsStaffEditorPermissions]

    

class SingleDrink(mixins.UserQuerySetMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = soda.objects.all()
    serializer_class = sodaserializer
    permission_classes =[IsStaffEditorPermissions]

    