from django.contrib import admin


from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'is_mvp', 'hire_date']
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    search_fields = ('name', 'id', 'phone', 'email')

admin.site.register(Realtor, RealtorAdmin)
