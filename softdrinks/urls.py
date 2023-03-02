from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.DrinksList.as_view(),name='soda-home'),
    path('home/mine/',views.MyDrinks.as_view(),name='soda-mine'),
    path('soda/<int:pk>/',views.SingleDrink.as_view(),name='soda-detail'),

]
