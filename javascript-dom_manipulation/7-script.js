fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results;
    const list = document.querySelector('#list_movies');

    movies.forEach(function (movie) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      list.appendChild(li);
    });
  })
  .catch(function (error) {
    console.error('Error:', error);
  });
