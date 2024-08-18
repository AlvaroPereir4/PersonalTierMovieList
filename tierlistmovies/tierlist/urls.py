from django.urls import path
from tierlist.views import index
from . import views

urlpatterns = [
    path('', index),
    path('search/', views.search_movie, name='search_movie') ### att dps
]
