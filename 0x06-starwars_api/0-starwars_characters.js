#!/usr/bin/node

const request = require('request-promise');

async function getMovieCharacters () {
  try {
    const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

    const movieResponse = await request({ uri: movieUrl, json: true });
    const charactersUrl = movieResponse.characters;

    for (const url of charactersUrl) {
      const characterResponse = await request({ uri: url, json: true });
      console.log(characterResponse.name);
    }
  } catch (error) {
    console.error('Error: ', error.message);
  }
}

getMovieCharacters();
