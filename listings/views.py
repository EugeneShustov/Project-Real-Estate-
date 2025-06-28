from django.shortcuts import render
from .models import Listing
from django.db.models import Q

def index(request):
    return render(request, 'listings/index.html')

def search(request):
    return render(request, 'listings/search.html')

def search(request):
    query = request.GET.get('q')
    results = Listing.objects.all()

    if query:
        results = results.filter(
            Q(title__icontains=query) |
            Q(city__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'listings/search.html', {'listings': results, 'query': query})