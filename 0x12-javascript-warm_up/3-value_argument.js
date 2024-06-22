#!/usr/bin/node

const { argv } = require('node:process');
let i = 0;

while (argv[i] !== undefined) i += 1;

if (i === 2) console.log('No argument'); else console.log(argv[2]);
