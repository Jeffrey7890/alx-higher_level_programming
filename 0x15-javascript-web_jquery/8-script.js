$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  data.results.forEach(function (film) {
    const listItem = $('<li>').text(film.title);
    $('#list_movies').append(listItem);
  });
});
