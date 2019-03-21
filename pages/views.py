from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'listings' : listings
    }

    return render(request, 'pages/index.html', context)
    # return HttpResponse("<h1>Hello World</h1>")

def about(request):
    """ Get all realtors"""
    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    # mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': get_mvp()
    }

    return render(request, 'pages/about.html', context)

def get_mvp():
    """ Get all the MVPs"""
    return Realtor.objects.all().filter(is_mvp=True)
