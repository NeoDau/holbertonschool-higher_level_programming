#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
     			return ('Rectangle ' + {});
    		} else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let x = 0; x < this.height; x++) {
      let fila;
      for (let i = 0; i < this.width; i++) {
        fila += 'X';
      }
      console.log(fila);
    }
  }
}
module.exports = (Rectangle);
