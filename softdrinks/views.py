from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import sodaserializer
from rest_framework import authentication,permissions
from rest_framework import generics
from .models import soda
import json

class DrinksList(generics.ListCreateAPIView):
    queryset = soda.objects.all()
    serializer_class = sodaserializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes =[]

    

class SingleDrink(generics.RetrieveUpdateDestroyAPIView):
    queryset = soda.objects.all()
    serializer_class = sodaserializer
    