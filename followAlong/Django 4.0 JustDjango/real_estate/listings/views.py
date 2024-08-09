from django.shortcuts import redirect, render
from listings import migrations
from .models import Listings
from .forms import ListingForm

# Create your views here.
def listings_list(request):
    listings = Listings.objects.all()
    context = {
        "listings":listings
    }
    return render(request,"listings.html",context)

def listings_retrive(request,pk):
    listing = Listings.objects.get(id=pk)
    context = {
        "listing":listing
    }
    return render(request,"listing.html",context)

def listings_form(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listings/')
    context = {
        "form" : form
    }
    return render(request,"form.html",context)

def listings_update(request,pk):
    listing = Listings.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST,instance=listing)
        if form.is_valid():
            form.save()
            return redirect('../..')
    context = {
        "form" : form
    }
    return render(request,"form_update.html",context)

def listings_delete(request,pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect("../..")