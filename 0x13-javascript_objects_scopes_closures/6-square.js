#!/usr/bin/node

// Import the Square class
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const char = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
