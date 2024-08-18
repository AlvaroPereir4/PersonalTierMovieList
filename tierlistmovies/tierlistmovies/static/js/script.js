// static/js/script.js
function searchMovies() {
    const query = document.getElementById('search').value;
    fetch(`/search/?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Limpa resultados anteriores

            if (data.error) {
                resultsDiv.innerHTML = `<p>${data.error}</p>`;
                return;
            }

            // Adiciona informações do filme
            const title = document.createElement('h3');
            title.textContent = data.title;
            resultsDiv.appendChild(title);

            const year = document.createElement('p');
            year.textContent = `Year: ${data.year}`;
            resultsDiv.appendChild(year);

            const genres = document.createElement('p');
            genres.textContent = `Genres: ${data.genres.join(', ')}`;
            resultsDiv.appendChild(genres);

            const plot = document.createElement('p');
            plot.textContent = `Plot: ${data.plot}`;
            resultsDiv.appendChild(plot);

            // Adiciona o pôster do filme
            if (data.poster) {
                const img = document.createElement('img');
                img.src = data.poster;
                img.alt = `Poster of ${data.title}`;
                img.style.maxWidth = '200px'; // Ajuste o tamanho conforme necessário
                resultsDiv.appendChild(img);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('results').innerHTML = `<p>Erro na pesquisa.</p>`;
        });
}
