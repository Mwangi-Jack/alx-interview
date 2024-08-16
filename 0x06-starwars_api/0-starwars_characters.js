#!/usr/bin/node

const axios = require('axios').default;

async function getMovieCharacters () {
  const response = await axios.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`);
  const movieData = response.data;

  const movieCharacters = movieData.characters;

  for (const url of movieCharacters) {
    const resp = await axios.get(url);
    const characterData = resp.data;

    console.log(characterData.name);
  }
}

getMovieCharacters();
