from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'realtor', 'list_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('realtor', 'title')
    list_per_page = 20
    search_fields = ('title', 'price', 'realtor', 'list_date', 'city', 'state')



admin.site.register(Listing, ListingAdmin)