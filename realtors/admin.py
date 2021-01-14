from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'phone', 'hire_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)
    list_filter = ('name',)
    list_per_page = 20
    search_fields = ('name', 'description','email')



admin.site.register(Realtor, RealtorAdmin)