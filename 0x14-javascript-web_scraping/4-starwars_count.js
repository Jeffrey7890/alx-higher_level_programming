#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

const ID = 18;

if (!URL) {
  process.exit(1);
}
request(URL, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  const data = JSON.parse(body);
  const filteredMovies = data.results.filter(movie => movie.characters.some(characterUrl => characterUrl.endsWith(`/${ID}/`)));

  console.log(filteredMovies.length);
});
