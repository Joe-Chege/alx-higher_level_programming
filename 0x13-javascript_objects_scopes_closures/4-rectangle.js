#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {}; // Return an empty object if w or h is not positive
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    // Exchange the width and height of the rectangle
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Double the width and height of the rectangle
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
