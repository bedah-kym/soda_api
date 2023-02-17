from django.contrib import admin
from django.urls import path
from . import views

app_name="softdrinks"

urlpatterns=[
    path('home/',views.drinks_list,name='home'),
    path('soda/<str:name>/',views.single_drink,name='single_drink'),

]
