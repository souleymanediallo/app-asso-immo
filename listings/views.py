from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Listing


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
    model = Listing
    template_name = "listings/listing_form.html"
    fields = ['title', 'address', 'zipcode', 'city', 'description', 'price', 'bedrooms', 'bathrooms', 'garage',
              'size', 'conditioner', 'pool', 'fireplace', 'alarm', 'photo_main', 'photo_1', 'photo_2', 'photo_3',
              'photo_4', 'photo_5', 'photo_6'
              ]
    context_object_name = "form"

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)



