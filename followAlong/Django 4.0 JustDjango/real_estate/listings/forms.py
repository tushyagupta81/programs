from dataclasses import fields
from django.forms import ModelForm
from .models import Listings
class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = [
            "title",
            "price",
            "num_bathrooms",
            "num_bedrooms",
            "square_footage",
            "address",
            ]