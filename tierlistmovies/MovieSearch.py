from imdb import Cinemagoer
import requests

class MovieSearch:
    def __init__(self):
        self.ia = Cinemagoer()
        pass

    def movie_request(self, search):
        response = [] ### criar uma clase das responses
        
        movies = self.ia.search_movie(search)
        if not movies:
            response.append("No movies found.")
            return response

        movie = movies[0]
        self.ia.update(movie)

        response = {
            'title': movie.get('title', 'N/A'),
            'year': movie.get('year', 'N/A'),
            'genres': movie.get('genres', []),
            'plot': movie.get('plot', ['N/A'])[0],
            'poster_url': movie.get('full-size cover url', movie.get('cover url', ''))
        }

        # Baixar o pôster
        poster_url = response['poster_url']
        if poster_url:
            response['poster'] = poster_url
            img_response = requests.get(poster_url)
            if img_response.status_code == 200:
                    # Opcional: Salvar o pôster localmente, se necessário
                with open(f"{movie['title']}_poster.jpg", 'wb') as file:
                    file.write(img_response.content)
            
        return response

if __name__ == "__main__":
    search_query = "Toy Story"  # Substitua pelo filme desejado
    movie_search = MovieSearch()
    result = movie_search.movie_request(search_query)
    for line in result:
        print(line)