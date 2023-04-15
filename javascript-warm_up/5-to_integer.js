#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + num);
}
