from .serializers import sodaserializer
from rest_framework import authentication
from rest_framework import generics
from .models import soda
from .permissions import IsStaffEditorPermissions

class DrinksList(generics.ListCreateAPIView):
    queryset = soda.objects.all()
    serializer_class = sodaserializer
    permission_classes =[IsStaffEditorPermissions]

    

class SingleDrink(generics.RetrieveUpdateDestroyAPIView):
    queryset = soda.objects.all()
    serializer_class = sodaserializer
    permission_classes =[IsStaffEditorPermissions]

    