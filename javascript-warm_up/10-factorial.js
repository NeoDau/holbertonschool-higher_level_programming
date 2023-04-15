#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const args = process.argv.slice(2);
const numero = parseInt(args);
console.log(factorial(numero));
