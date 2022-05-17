from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path("ajout/",views.ajout),
    path("revu/",views.revu),
    path("index",views.index),
    path("",views.centre),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/",views.update),
    path("updaterevu/<int:id>/", views.updaterevu),
    path("delete/<int:id>/",views.delete),
    path("ajoutsite/",views.ajoutsite),
    path("revusite/",views.revusite),
    path("indexsite/",views.indexsite),
    path("affichesite/<int:id>/", views.affichesite),
    path("updatesite/<int:id>/",views.updatesite),
    path("updaterevusite/<int:id>/", views.updaterevusite),
    path("deletesite/<int:id>/",views.deletesite),
]