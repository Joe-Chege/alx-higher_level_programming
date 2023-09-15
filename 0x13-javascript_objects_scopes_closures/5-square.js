#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // Assuming your Rectangle class is in a separate file named '4-rectangle.js'

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle with size for both width and height
  }
}

module.exports = Square;
