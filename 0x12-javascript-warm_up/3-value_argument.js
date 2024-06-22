#!/usr/bin/node

const { argv } = require('node:process');

const length = argv.length;

if (length === 2) { console.log('No argument'); } else console.log(argv[2]);
