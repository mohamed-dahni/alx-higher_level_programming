#!/usr/bin/node
const request = require('request');

const getCharacterData = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(new Error(`Error occurred while fetching character: ${error.message}`));
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character data. Status code: ${response.statusCode}`));
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
};

const getMovieData = async (movieId) => {
  return new Promise((resolve, reject) => {
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    request.get(apiUrl, (error, response, body) => {
      if (error) {
        reject(new Error(`Error occurred: ${error.message}`));
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch data. Status code: ${response.statusCode}`));
      } else {
        const movieData = JSON.parse(body);
        resolve(movieData.characters);
      }
    });
  });
};

const printCharacters = async (movieId) => {
  try {
    const characterUrls = await getMovieData(movieId);

    for (const characterUrl of characterUrls) {
      const characterName = await getCharacterData(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error.message);
  }
};

const movieId = process.argv[2];
printCharacters(movieId);
