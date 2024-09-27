#!/usr/bin/node

const { list } = require('./100-data');

// create a new array with each value multiplied by its index
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
