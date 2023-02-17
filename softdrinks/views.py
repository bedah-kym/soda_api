from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import sodaserializer
from .models import soda


@api_view(['GET','POST'])
def drinks_list(request,format=None):
    drinks = soda.objects.all()
    if request.method == 'GET':
        serializer = sodaserializer(drinks,many=True)
        return JsonResponse({'drinks':serializer.data})
    if request.method == 'POST':
        serializer = sodaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def single_drink(request,name,format=None):
    drink = get_object_or_404(soda,brand=name)

    if request.method == 'GET':
        serializer = sodaserializer(drink,many=False)
        return JsonResponse({'drink':serializer.data})
    #put/update is similar to create so you need to pass in data to the serializer
    if request.method == 'PUT':
        serializer = sodaserializer(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status = status.HTTP_401_BAD_REQUEST)

    if request.method == 'DELETE':
        drink.delete()
