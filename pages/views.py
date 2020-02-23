from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choice import bedrooms, states, prices

def index(request):
    listing_qs = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]
    context = {
        'home_listing': listing_qs,
        'bedrooms': bedrooms,
        'states': states,
        'prices': prices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    about_realtors = Realtor.objects.order_by('hire_date')[:3]
    is_mvp = Realtor.objects.filter(is_mvp=True)
    context = {
        'teams': about_realtors,
        'seller_of_month': is_mvp
    }
    return render(request, 'pages/about.html', context)


