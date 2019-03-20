from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing


def index(request):
    """Obtengo el listado de la bd, y armo el paginator para la paginación"""

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # en lugar de usar .all, ordena por esa property en forma descendente con el -
    # el .filter es para filtrar por alguna condicion

    paginator = Paginator(listings, 6) # límite de objs x página
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


    # return render(request, 'listings/listings.html')
