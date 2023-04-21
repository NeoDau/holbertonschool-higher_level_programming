#!/usr/bin/node

$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function () {
    $('header').text('Neo xD');
  });
});
