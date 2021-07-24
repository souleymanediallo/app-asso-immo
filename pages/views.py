from django.shortcuts import render
from listings.models import Listing
from .choices import bedroom_choices, price_choices, city_choices


# Create your views here.
def home(request):
    listings = Listing.objects.all()[:2]
    context = {
        'listings': listings,
        'city_choices': city_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, "pages/index.html", context)


def search(request):
    listings = Listing.objects.all()
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__iexact=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    context = {
        'listings': listings,
        'city_choices': city_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'values': request.GET,
    }
    return render(request, "pages/search.html", context)


def about(request):
    return render(request, "pages/association.html")


def mentions(request):
    return render(request, "pages/mentions-legales.html")
