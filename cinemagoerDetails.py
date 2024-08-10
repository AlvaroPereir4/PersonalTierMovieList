from imdb import Cinemagoer
import requests


ia = Cinemagoer()
movies = ia.search_movie('Inception')
movie = movies[0]
ia.update(movie)

print(f"Title: {movie['title']}")
print(f"Year: {movie['year']}")
print(f"Genres: {', '.join(movie['genres'])}")
print(f"Plot: {movie['plot'][0]}")

poster_url = movie.get('full-size cover url', None)
if not poster_url:
    poster_url = movie.get('cover url', None)

if poster_url:
    print(f"Poster URL: {poster_url}")
    response = requests.get(poster_url)
    if response.status_code == 200:
        with open(f"{movie['title']}_poster.jpg", 'wb') as file:
            file.write(response.content)
        print("Poster downloaded successfully.")
    else:
        print("Failed to download poster.")
else:
    print("Poster URL not found.")