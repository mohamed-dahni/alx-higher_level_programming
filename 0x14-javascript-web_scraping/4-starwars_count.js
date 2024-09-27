#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error occurred: ${error.message}`);
    return;
  }
  try {
    const results = JSON.parse(body).results;
    const count = results.reduce((acc, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/')) ? acc + 1 : acc;
    }, 0);

    console.log(count);
  } catch (parseError) {
    console.error(`Error parsing JSON: ${parseError.message}`);
  }
});
