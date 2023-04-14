#!/usr/bin/node

const [primerPalabra] = process.argv.slice(2);
const [segundaPalabra] = process.argv.slice(3);

if (primerPalabra + segundaPalabra) {
  console.log(primerPalabra + ' is ' + segundaPalabra);
} else {
  console.log('undefined is undefined');
}
