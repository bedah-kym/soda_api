from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import sodaserializer
from rest_framework.views import APIView
from .models import soda
import json

class DrinksList(APIView):
    
    def get(self,request,format=None):
        drinks = soda.objects.all()
        serializer = sodaserializer(drinks,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = sodaserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    

class SingleDrink(APIView):
    def get(self,request,name,format=None):
        drink = get_object_or_404(soda,brand=name)
        serializer = sodaserializer(drink)
        return Response(serializer.data)

    def put(self,request,name,format=None):
        #get the drink,serialize it ,if valid save it else dump errors
        drink = get_object_or_404(soda,brand=name)
        serializer = sodaserializer(drink, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,name,format=None):
        drink = get_object_or_404(soda,brand=name)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

