from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'realtor', 'title','is_published', 'price', 'list_date']
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price', 'address', 'city','zipcode','realtor__name')
    
    
admin.site.register(Listing, ListingAdmin)
