#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

if (!URL) {
  process.exit(1);
}
request(URL, (error, response) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  console.log('code: ', response.statusCode);
});
