#!/usr/bin/node

const fs = require('fs');

const filePath = './my_file.txt';
const content = 'Python is cool';

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
