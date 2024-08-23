from django.urls import path
from tierlist.views import index
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index),
    path('search/', views.search_movie, name='search_movie') ### att dps
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
