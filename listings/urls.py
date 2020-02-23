from django.urls import path  

from .views import listings, single_listing, search

app_name = 'listings'

urlpatterns = [
    path("", listings, name='listings'),
    path('detail/<int:pk>/', single_listing, name='single_listing'),
    path('search/', search, name='search')
]



