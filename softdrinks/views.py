from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import sodaserializer
from .models import soda
import json

@api_view(['GET','POST'])
def drinks_list(request,format=None,*args,**kwargs):
    drinks = soda.objects.all()
    if request.method == 'GET':
        serializer = sodaserializer(drinks,many=True)
        return Response({'drinks':serializer.data})
        #return JsonResponse(body)
    if request.method == 'POST':
        serializer = sodaserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def single_drink(request,name,format=None):
    drink = get_object_or_404(soda,brand=name)
    instance =  sodaserializer(drink)

    if request.method == 'GET':
        serializer = sodaserializer(drink)
        return Response({'drink':serializer.data})
    #put/update is similar to create so you need to pass in data to the serializer
    if request.method == 'PUT':
        serializer = sodaserializer(drink,data=request.data)
        brand = serializer.initial_data.get('brand')
        if brand is None:
            serializer["brand"]="new"

        if serializer.is_valid(raise_exception=True):
            
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        drink.delete()
