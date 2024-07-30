#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api/films/';

const URLID = URL + process.argv[2] + '/';

if (!URLID) {
  process.exit(1);
}
request(URLID, (error, response) => {
  if (error) {
    process.exit(1);
  }

  const movie = JSON.parse(response.body);

  console.log(movie.title);
});
