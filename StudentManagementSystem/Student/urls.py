from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path("",views.index,name="index"),
]
