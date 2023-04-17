#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected response: ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', error => {
    if (error) {
      console.error(error);
      return;
    }

    console.log(`Successfully wrote file to ${filePath}`);
  });
});
