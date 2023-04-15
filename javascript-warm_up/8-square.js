#!/usr/bin/node

const args = process.argv.slice(2);
const equis = parseInt(args);

if (isNaN(equis)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < equis; x++) {
    let fila = '';
    for (let r = 0; r < equis; r++) {
      fila += 'X';
    }
    console.log(fila);
  }
}
