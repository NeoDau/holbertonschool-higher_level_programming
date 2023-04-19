#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

function error (err) {
  if (err) {
    console.log(err);
  }
}

fs.writeFile(filePath, content, 'utf-8', error);
