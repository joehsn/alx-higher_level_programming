#!/usr/bin/node

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (char = 'X') {
    if (this.width && this.height) {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          output += char;
        }
        output += '\n';
      }
      console.log(output.slice(0, -1));
    } else {
      console.log('Width or height is not a positive integer');
    }
  }
}

module.exports = Square;
