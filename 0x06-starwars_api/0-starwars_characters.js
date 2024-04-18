#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Create an array to store promises for fetching character data
  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject('Error fetching character data: ' + error);
          return;
        }

        if (response.statusCode !== 200) {
          reject('Failed to fetch character data: ' + response.statusCode);
          return;
        }

        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  });

  // Wait for all character requests to complete
  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});
