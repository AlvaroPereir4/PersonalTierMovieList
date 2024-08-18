from django.contrib import admin
from django.urls import path
from tierlist import views

urlpatterns = [
    path('', views.teste, name='teste'),
]
