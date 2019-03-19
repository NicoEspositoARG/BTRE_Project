from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name ='index'),  # al estar vacio el primer parámetro es el root.
    path('about', views.about, name ='about')  #el primer parametro es lo que va en la url de la ruta.
    
]