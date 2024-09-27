#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error occurred: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Error occurred while fetching character: ${charError.message}`);
        } else if (charResponse.statusCode !== 200) {
          console.error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
