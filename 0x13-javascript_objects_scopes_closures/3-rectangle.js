#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let display = '';
    for (let j = 0; j < this.width; j++) {
      display += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(display);
    }
  }
}
module.exports = Rectangle;
