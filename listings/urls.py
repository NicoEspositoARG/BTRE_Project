from django.urls import path

from . import views

# se vincula desde el btre urls.py para que cualquier /listings se consulte en este archivo

urlpatterns = [
    path('', views.index, name='listings'),  # si está vacio '' se refiere a /listings
    path('<int:listing_id>', views.listing, name='listing'),  # /listings/35
    path('search', views.search, name='search'),  # listings/search 

]