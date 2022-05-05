from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path("ajout/",views.ajout),
    path("revu/",views.revu),
    path(""),view.index),
]