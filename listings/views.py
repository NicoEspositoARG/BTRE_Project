from django.shortcuts import render, get_object_or_404

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


def index(request):
    """Obtengo el listado de la bd, y armo el paginator para la paginación"""

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # en lugar de usar .all, ordena por esa property en forma descendente con el -
    # el .filter es para filtrar por alguna condicion
    # [:3] seguido al parentesis me limita a solo 3 resultados.

    paginator = Paginator(listings, 6)  # límite de objs x página
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """ Get one specific listing object """
    listing = get_object_or_404(Listing, pk=listing_id)
    # va a chequear si existe el obj con el id que recibió

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'] # IMPORTANTE #
        # el GET [] busca el name del atribute html, si no definimos el name no lo va a traer
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) # búsqueda en contenido

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) # búsqueda exacta, case insensitive

    # City
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # up to entry, less than or equal to

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # up to entry, less than or equal to

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET # esto es para mantener los valores de búsqueda
    }

    return render(request, 'listings/search.html', context)

