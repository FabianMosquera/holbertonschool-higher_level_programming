#!/usr/bin/node
// JS function that prints the number of arguments already
let n = 0;
exports.logMe = function (item) {
  console.log(n + ': ' + item);
  n++;
};
