#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const URL = process.argv[2];

const file = process.argv[3];

if (!URL) {
  process.exit(1);
}
request(URL, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  fs.writeFile(file, body, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }
  });
});
