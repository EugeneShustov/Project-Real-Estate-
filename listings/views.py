from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Listing, Comment
from .forms import CommentForm, SignUpForm


def index(request):
    return render(request, 'listings/index.html')

def search(request):
    query = request.GET.get('q')
    results = Listing.objects.all()

    if query:
        results = results.filter(
            Q(title__icontains=query) |
            Q(city__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'listings/search.html', {
        'listings': results,
        'query': query }
                  )

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    comments = listing.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.listing = listing
            comment.save()
            return redirect('listing_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'listings/listing_view.html', {
        'listing': listing,
        'comments': comments,
        'form': form
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def home_view(request):
    listings = Listing.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'users/home.html', {'listings': listings})


