#!/usr/bin/node

const fs = require('fs');

const filePath = './myFile.txt';
const content = 'Python is cool';

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
