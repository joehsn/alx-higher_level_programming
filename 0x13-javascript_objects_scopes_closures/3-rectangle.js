#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    if (this.width && this.height) { // Check if valid rectangle exists
      let output = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          output += 'X';
        }
        output += '\n'; // Add newline after each row
      }
      console.log(output.slice(0, -1)); // Remove the last newline
    } else {
      console.log('Width or height is not a positive integer');
    }
  }
}

module.exports = Rectangle;
