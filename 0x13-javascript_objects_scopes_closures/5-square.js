#!/usr/bin/node

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call Rectangle constructor with size for both width and height
  }
}

module.exports = Square;
