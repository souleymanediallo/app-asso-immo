from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Listing
from .forms import ListingForm


# Create your views here.
class ListingsListView(ListView):
    model = Listing
    template_name = "listings/listing_list.html"
    context_object_name = "listings"


class ListingsDetail(LoginRequiredMixin, DetailView):
    model = Listing
    template_name = "listings/listing_detail.html"
    context_object_name = "listing"


class ListingsCreateView(LoginRequiredMixin, CreateView):
    form_class = ListingForm
    template_name = "listings/listing_form.html"
    context_object_name = "form"
    success_url = "/listing/"

    def form_valid(self, form):
        form.instance.realtor = self.request.user.profile
        return super().form_valid(form)


class ListingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    fields = [
        'title',
        'address',
        'zipcode',
        'city',
        'description',
        'price',
        'bedrooms',
        'bathrooms',
        'garage',
        'size',
        'conditioner',
        'pool',
        'fireplace',
        'alarm',
        'photo_main',
        'photo_1',
        'photo_2',
        'photo_3',
        'photo_4',
        'photo_5',
        'photo_6'
    ]

    def form_valid(self, form):
        form.instance.realtor = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        if self.request.user.profile == listing.realtor:
            return True
        return False


class ListingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = '/'

    def test_func(self):
        listing = self.get_object()
        if self.request.user.profile == listing.realtor:
            return True
        return False


@login_required
def my_listing(request):
    listings = Listing.objects.filter(realtor=request.user.profile)
    context = {"listings": listings}
    return render(request, "listings/my_listing.html", context)
