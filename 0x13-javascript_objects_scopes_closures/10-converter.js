#!/usr/bin/node
// JS function that converts a number from base 10
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
