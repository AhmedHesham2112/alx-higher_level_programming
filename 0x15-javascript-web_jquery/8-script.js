$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (films) {
  $.each(films.results, function (index, film) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  });
});
