from django.contrib import admin
from django.urls import path
from . import views

app_name="softdrinks"

urlpatterns=[
    path('home/',views.DrinksList.as_view(),name='home'),
    path('soda/<int:pk>/',views.SingleDrink.as_view(),name='single_drink'),

]
