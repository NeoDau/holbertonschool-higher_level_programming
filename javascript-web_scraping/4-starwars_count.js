#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected response: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const wedgeFilms = filmData.results.filter(film => {
    return film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`);
  });
  console.log(`${wedgeFilms.length}`);
});
