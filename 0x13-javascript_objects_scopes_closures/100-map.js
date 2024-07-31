#!/usr/bin/node
const list = require('./100-data').list;

const newList = list.map((e1, idx) => e1 * idx);
console.log(list);
console.log(newList);
