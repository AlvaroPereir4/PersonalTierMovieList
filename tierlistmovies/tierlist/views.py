# views.py
from django.shortcuts import render
from django.http import JsonResponse
from MovieSearch import MovieSearch  # Certifique-se de que MovieSearch está no mesmo diretório


def index(request):
    return render(request, 'index.html')

def search_movie(request):
    search_query = request.GET.get('query', '')
    if search_query:
        movie_search = MovieSearch()
        results = movie_search.movie_request(search_query)
        return JsonResponse(results)
    return JsonResponse({'error': 'No search query provided'}, status=400)
