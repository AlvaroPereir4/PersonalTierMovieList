from django.urls import path
from tierlist.views import index

urlpatterns = [
    path('', index)
]
