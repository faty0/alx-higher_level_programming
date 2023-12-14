#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else {
      let display = '';
      for (let i = 0; i < this.width; i++) {
        display += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(display);
      }
    }
  }
}
module.exports = Square;
