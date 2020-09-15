#!/usr/bin/node
// JS prints the addition of 2 integers

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(firstInt, secondInt);
