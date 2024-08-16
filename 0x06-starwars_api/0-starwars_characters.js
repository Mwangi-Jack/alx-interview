#!/usr/bin/node

const axios = require('axios').default;

const movieID = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api';

async function getMovieCharacters () {
  if (movieID) {
    const response = await axios.get(`${baseUrl}/films/${movieID}`);
    const movieData = response.data;

    const movieCharacters = movieData.characters;

    for (const url of movieCharacters) {
      const resp = await axios.get(url);
      const characterData = resp.data;

      console.log(characterData.name);
    }
  } else {
    console.log('Pleas provide Movie ID');
  }
}

getMovieCharacters();
