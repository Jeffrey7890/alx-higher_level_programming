#!/usr/bin/node

const { argv } = require('node:process');

const size = Number(argv[2]);
let string = '';

if (isNaN(size)) console.log('Missing size'); else for (let i = 0; i < size; i++) { for (let j = 0; j < size; j++) { string += 'X'; } console.log(string); string = ''; }
