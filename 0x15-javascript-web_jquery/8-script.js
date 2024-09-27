$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const listMovies = $('#list_movies');
    data.results.forEach(function (movie) {
      listMovies.append('<li>' + movie.title + '</li>');
    });
  });
});
