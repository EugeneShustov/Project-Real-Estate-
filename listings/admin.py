from django.contrib import admin
from .models import Listing, YourModel

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'city')

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'city')
