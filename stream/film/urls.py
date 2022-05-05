from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path("ajout/",views.ajout),
    path("revu/",views.revu),
    path("",views.index),
    path("affiche/<int:id>/", views.affiche),
    path ("update/<int:id>/",views.update),
    path("updaterevu/<int:id>/", views.updaterevu),
]