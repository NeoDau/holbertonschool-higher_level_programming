#!/usr/bin/node

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (movie) {
    const movieList = $('UL#list_movies');
    for (let i = 0; i < movie.results.length; i++) {
      movieList.append(`<li>${movie.results[i].title}</li>`);
    }
  });
});
