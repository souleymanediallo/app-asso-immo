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