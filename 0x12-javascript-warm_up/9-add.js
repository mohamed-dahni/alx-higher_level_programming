#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  console.log(c);
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

add(Number(arg1, arg2));
