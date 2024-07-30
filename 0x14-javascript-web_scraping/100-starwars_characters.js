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

  const characters = movie.characters;
  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response) => {
        if (error) {
          return reject(error);
        }
        try {
          const person = JSON.parse(response.body);
          resolve(person.name);
        } catch (e) {
          reject(e);
        }
      });
    });
  });
  Promise.all(characterPromises)
    .then(characterNames => {
      console.log(characterNames.join('\n'));
    })
    .catch(error => {
      console.error(error);
    });
});
