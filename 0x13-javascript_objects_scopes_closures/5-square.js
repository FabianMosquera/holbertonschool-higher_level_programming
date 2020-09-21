#!/usr/bin/node
// JS class Square that defines a square
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
