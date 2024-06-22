#!/usr/bin/node

const { argv } = require('node:process');

let a = Number(argv[2]);
let b = 0;
const length = argv.length;

for (let i = 3; i < length; i++) { if (Number(argv[i + 1]) > a) { b = a; a = Number(argv[i + 1]); } }

console.log(b);
