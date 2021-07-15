from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/association.html")


def mentions(request):
    return render(request, "pages/mentions-legales.html")