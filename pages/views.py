from django.shortcuts import render
from listings.models import Realtor, Listing


# Create your views here.
def home(request):
    listings = Listing.objects.all()[:2]
    context = {'listings': listings}
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/association.html")


def mentions(request):
    return render(request, "pages/mentions-legales.html")
