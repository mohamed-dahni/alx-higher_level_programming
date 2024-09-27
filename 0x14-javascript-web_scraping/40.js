#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error occurred: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesMovies = filmsData.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    console.log(`${wedgeAntillesMovies.length}`);
  }
});
