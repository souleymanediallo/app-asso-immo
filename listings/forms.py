from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
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

        labels = {
            'title': "Titre",
            'address': "Adresse",
        }
