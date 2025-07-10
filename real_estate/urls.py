from django.urls import path
from listings import views as listings_views
from listings.views import signup_view, login_view, logout_view, home_view

urlpatterns = [
 path('', listings_views.index, name='index'),
 path('search/', listings_views.search, name='search'),
 path('listings/<int:pk>/', listings_views.listing_detail, name='listing_detail'),

 path('signup/', signup_view, name='signup'),
 path('login/', login_view, name='login'),
 path('logout/', logout_view, name='logout'),
 path('', home_view, name='home'),
]

