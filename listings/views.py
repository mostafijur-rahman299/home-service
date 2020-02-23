from django.shortcuts import render

from .models import Listing

from django.core.paginator import Paginator

from .choice import bedrooms, states, prices


def listings(request):
    listings_qs = Listing.objects.filter(is_published=True)
    
    paginator = Paginator(listings_qs, 12) # Show 10 contacts per page
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    
    return render(request, 'listings/list.html', {'listings': page_listings})

def single_listing(request, pk):
    listing = Listing.objects.get(pk=pk)
    return render(request, 'listings/single_listing.html', {'object': listing})



def search(request):
    query_list = Listing.objects.order_by("-list_date")
    
    # keywords 
    if "keywords" in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)
            
    # city 
    if "city" in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
            
    # state 
    if "state" in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)
    
    # bedrooms 
    if "bedrooms" in request.GET:
        bedroom = request.GET['bedrooms']
        if bedroom:
            query_list = query_list.filter(bedrooms__lte=bedroom)
        
    # price 
    if "price" in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)
        
    
        
    context = {
        'states': states,
        'prices': prices, 
        'bedrooms': bedrooms,
        'listings': query_list
    }
    return render(request, 'listings/search.html', context)


